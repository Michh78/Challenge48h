# **Analyse des Tweets Clients d'Engie et Paramétrage d'Agents IA**

## **1. Introduction**
Ce projet vise à analyser les tweets des clients d'Engie afin d'identifier les tendances, d'extraire des KPI pertinents, d'effectuer une analyse de sentiment et de paramétrer des agents IA capables de classifier automatiquement les réclamations des clients.

---

## **2. Méthodologie Utilisée**

### **2.1 Prétraitement des Données**
1. Chargement des tweets depuis un fichier CSV.
2. Nettoyage des données :
   - Suppression des valeurs manquantes
   - Suppression des colonnes inutiles
   - Conversion des dates en format datetime
   - Formatage des identifiants (id)
3. Extraction d'informations utiles :
   - Longueur des tweets
   - Présence de mots-clés critiques
   - Détection des mentions de @Engie

### **2.2 Extraction des KPI**
- Nombre de tweets par jour/semaine/mois
- Nombre de mentions de @Engie
- Nombre de tweets contenant des mots-clés critiques (“panne”, “urgence”, “facture”...)
- Répartition des sentiments des tweets

### **2.3 Analyse de Sentiment**
- Utilisation d'un modèle NLP pré-entraitné (VADER, Mistral AI)
- Classification des tweets en **positif, neutre, négatif**
- Visualisation de la répartition des sentiments

### **2.4 Paramétrage des Agents IA (Mistral AI)**
1. Entraînement d'un agent IA à classifier les types de réclamations.
    - Création d'un agent via Mistral AI avec des instructions spécifiques.
    - Définition de prompts et de modèles d'entraînement.
    - Ajustement des réponses en fonction des tests et des retours.
2. Catégories détectées :
   - **Problèmes de facturation** (erreurs, prélèvements injustifiés)
   - **Pannes & urgences** (gaz, électricité, eau chaude)
   - **Service client injoignable** (absence de réponse, relances)
   - **Problèmes avec l'application** (bugs, pannes)
   - **Délais d'intervention trop longs**
3. Calcul d'un **score d'inconfort** (0 à 100%)
     - Évaluation basée sur la gravité des plaintes et leur fréquence.
4. Génération automatique de réponses (option bonus)
     - Création de modèles de réponse pour guider les utilisateurs vers des solutions.

---

## **3. Technologies Utilisées**
- **Python** : Pandas, Matplotlib, Seaborn.
- **IA/NLP** : Mistral AI
- **Base de Données** : CSV
- **Visualisation** : Power BI 

---

## **4. Exécution du Projet**

### **4.1 Installation des Dépendances**
```bash
pip install pandas numpy matplotlib seaborn mistralai
```

### **4.2 Prétraitement des Données**
```bash
python data_cleaning.py
```

### **4.3 Extraction des KPI**
```bash
python kpi_extraction.py
```

### **4.4 Analyse de Sentiment**
```bash
python sentiment_analysis.py
```

### **4.5 Paramétrage de l'Agent IA**
```bash
python ai_agent.py
```

### **4.6 Lancement du Tableau de Bord (Power BI)**
```bash

```

---

## **5. Exemples d'Interactions avec l'Agent IA**

### **Prompt envoyé à l'agent Mistral :**
```
Classifie ce tweet dans l'une des catégories suivantes :
- Facturation
- Pannes & urgences
- Service client injoignable
- Application
- Délai d'intervention
Tweet : "Mon compteur ne fonctionne plus depuis 3 jours, service client injoignable !"
```

### **Réponse attendue :**
```
Catégorie : Pannes & urgences
Score d'inconfort : 85%
Action suggérée : Contacter le service technique Engie en priorité.
```

---

## **6. Auteurs & Contact**
Projet réalisé dans le cadre du Hackathon Engie 2025.

- **Participants** : Belicia, Julie, Michel, Guillaume, Owandji.

---

**Hackathon groupe 14 ! 🚀**
