import pandas as pd

# Charger le fichier en détectant le bon séparateur
df = pd.read_csv("filtered_tweets_engie.csv", sep=";", engine="python", dtype={"id": str})

df.columns = df.columns.str.replace("\ufeff", "")  # Supprime le BOM


df = df.drop(columns=["name", "screen_name"])

# # Convertir l'ID en entier
# df["id"] = df["id"].apply(lambda x: int(float(x)))

# Convertir `created_at` en datetime (et corriger le fuseau horaire)
df["created_at"] = pd.to_datetime(df["created_at"], errors='coerce', utc=True)

# Formater la colonne `created_at` au format jj/mm/aa
df['hour'] = df['created_at'].dt.hour
df['weekday'] = df['created_at'].dt.day_name()
df["created_at"] = df["created_at"].dt.strftime("%d/%m/%y")

# Supprimer les colonnes vides (si présentes)
df = df.dropna(axis=1, how="all")

# Nettoyer le texte (supprimer les \n)
df["full_text"] = df["full_text"].str.replace(r"\n", " ", regex=True)

# Afficher un aperçu
print(df.head())

# Sauvegarde du fichier nettoyé
df.to_csv("clean_tweets.csv", sep=";", index=False)