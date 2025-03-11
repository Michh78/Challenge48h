import pandas as pd
import requests
import time
import json
import re

# ✅ Ta clé API Mistral AI officielle
api_key = "6g6xigB7h7XjaMMvKtw9Mu97NaZD9T2T"
url = "https://api.mistral.ai/v1/chat/completions"  # API officielle

# ✅ Headers d'authentification
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# ✅ Charger le CSV
df = pd.read_csv(
    r"C:\\Users\\owand\\OneDrive\\Documents\\filtered_tweets_engie.csv",
    sep=';',
    quotechar='"',
    on_bad_lines='warn',
    index_col=False,
    encoding='utf-8'
)

print("Colonnes disponibles :", df.columns)

# ✅ Fonction pour analyser un batch (3 par 3 pour limiter)
def analyze_batch(tweets):
    tweets = [" ".join(t.split()[:20]) for t in tweets]  # Limite à 20 mots
    tweets_prompt = "\n".join([f"{i+1}. {t}" for i, t in enumerate(tweets)])

    # ✅ Prompt structuré avec 5 catégories et max 3 sous-catégories
    prompt = f"""
Voici les messages :
{tweets_prompt}

Pour chaque message, attribue :
- Une catégorie parmi : "Problèmes techniques", "Facturation", "Contrats", "Service client", "Délai d'intervention".
- Une sous-catégorie (max 3 par catégorie, exemples ci-dessous).
- Un score d'inconfort (0-100).

Sous-catégories :
Problèmes techniques : "Coupure d'électricité", "Problème de compteur", "Fuite de gaz"
Facturation : "Erreur de facturation", "Prélèvement injustifié", "Demande de remboursement"
Contrats : "Souscription", "Résiliation", "Changement de titulaire"
Service client : "Pas de réponse", "Réponse insatisfaisante", "Mauvaise prise en charge"
Délai d'intervention : "Retard de rendez-vous", "Retard de réparation", "Retard administratif"

Réponds uniquement sous ce format JSON pour chaque message :
{{
  "problem_type": "Catégorie",
  "more_detail": "Sous-catégorie",
  "discomfort_score": 0-100
}}

Un JSON par message, séparé par une ligne vide.
"""

    payload = {
        "model": "mistral-tiny",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code == 200:
            print("✅ Batch traité")
            time.sleep(2)
            return response.json()['choices'][0]['message']['content'].strip()
        else:
            print("❌ Erreur API:", response.status_code, response.text)
            return ""
    except requests.exceptions.Timeout:
        print("❌ Timeout dépassé, batch ignoré.")
        return ""
    except Exception as e:
        print("❌ Erreur:", e)
        return ""

# ✅ Fonction pour découper en batchs
def batch_list(lst, batch_size=3):
    for i in range(0, len(lst), batch_size):
        yield lst[i:i + batch_size]

# ✅ Fonction pour parser les JSON multiples
def parse_multiple_json_objects(response_text):
    json_objects = []
    matches = re.findall(r'\{.*?\}', response_text, re.DOTALL)
    for match in matches:
        try:
            json_obj = json.loads(match)
            json_objects.append(json_obj)
        except json.JSONDecodeError as e:
            print("❌ JSON invalide ignoré :", e)
    return json_objects

# ✅ Analyse complète
results = []
batch_size = 3  # Réduction à 3 pour limiter les erreurs
tweets_list = df['full_text'].astype(str).tolist()

for idx, batch in enumerate(batch_list(tweets_list, batch_size)):
    print(f"🔄 Analyse du batch {idx + 1}/{len(tweets_list) // batch_size + 1}")
    res = analyze_batch(batch)
    
    json_res = parse_multiple_json_objects(res)

    if len(json_res) != len(batch):
        print(f"⚠️ Problème batch {idx + 1}: {len(json_res)} réponses pour {len(batch)} tweets. Compléter avec UNKNOWN.")
        while len(json_res) < len(batch):
            json_res.append({"problem_type": "UNKNOWN", "more_detail": "UNKNOWN", "discomfort_score": 0})
        json_res = json_res[:len(batch)]

    results.extend(json_res)

# ✅ Vérification finale
print(f"Nombre total de réponses : {len(results)} pour {len(df)} tweets")

# ✅ Transformation en DataFrame
results_df = pd.DataFrame(results)
final_df = pd.concat([df.reset_index(drop=True), results_df.reset_index(drop=True)], axis=1)

# ✅ Sauvegarde finale
final_df.to_csv(r"C:\\Users\\owand\\OneDrive\\Documents\\filtered_tweets_categorie_inconfort.csv", sep=';', index=False)

print("🎉 Analyse complète terminée et fichier sauvegardé.")
