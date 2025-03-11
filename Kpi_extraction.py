#KPI EXTRACTION
import pandas as pd
import matplotlib.pyplot as plt
file_path = r"C:\Users\user\Downloads\clean_tweets.csv" 

# Attempt to read with different delimiters
try:
    df = pd.read_csv(file_path, delimiter=";", encoding="utf-8")  
except:
    df = pd.read_csv(file_path, delimiter=",", encoding="utf-8")  

df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce', utc=True)

# Group tweets 
tweets_per_day = df.groupby(df['created_at'].dt.date).size()

df['week'] = df['created_at'].dt.to_period('W')
tweets_per_week = df.groupby('week').size()

df['month'] = df['created_at'].dt.to_period('M')
tweets_per_month = df.groupby('month').size()

# Display results
print(f"Tweets per day:\n{tweets_per_day.head()}")
print(f"Tweets per week:\n{tweets_per_week.head()}")
print(f"Tweets per month:\n{tweets_per_month.head()}")

# Detect tweets mentioning @engie
df['mentions_engie'] = df['full_text'].str.contains(r'@engie', case=False, na=False)
engie_mentions_count = df['mentions_engie'].sum()
print(f"Total tweets mentioning @engie: {engie_mentions_count}")

# Define important keywords
critical_keywords = ["délai", "panne", "urgence", "scandale", "problème", "facture"]

# Check if a tweet contains any of these keywords
df['critical_tweet'] = df['full_text'].apply(lambda x: any(word in x.lower() for word in critical_keywords))

# Count critical tweets
critical_tweets_count = df['critical_tweet'].sum()

print(f"Total tweets with critical keywords: {critical_tweets_count}")

df.to_csv(r"C:\Users\user\Downloads\tweets_with_kpis.csv", index=False)
print("KPI data saved successfully!")


tweets_per_day = df.groupby(df['created_at'].dt.date).size()

plt.figure(figsize=(10, 5))
plt.plot(tweets_per_day.index, tweets_per_day.values, marker="o")
plt.xlabel("Date")
plt.ylabel("Number of Tweets")
plt.title("Tweets per Day")
plt.xticks(rotation=45)
plt.show()
