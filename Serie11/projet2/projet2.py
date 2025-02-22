import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

# Configuration de l'API Twitter
API_KEY = "votre_api_key"
API_SECRET = "votre_api_secret"
ACCESS_TOKEN = "votre_access_token"
ACCESS_SECRET = "votre_access_secret"

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def analyser_sentiment(mot_cle: str, nombre_tweets: int = 100, lang: str = "en"):
    try:
        tweets = api.search_tweets(q=mot_cle, count=nombre_tweets, lang=lang)
        positifs, negatifs, neutres = 0, 0, 0

        for tweet in tweets:
            texte = tweet.text
            blob = TextBlob(texte)
            polarite = blob.sentiment.polarity

            if polarite > 0:
                positifs += 1
            elif polarite < 0:
                negatifs += 1
            else:
                neutres += 1

        total = positifs + negatifs + neutres
        labels = ["Positifs", "Négatifs", "Neutres"]
        valeurs = [positifs, negatifs, neutres]

        plt.pie(valeurs, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title(f"Analyse de sentiment pour '{mot_cle}'")
        plt.show()

    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    mot_cle = input("Entrez un mot-clé à analyser : ")
    analyser_sentiment(mot_cle, 100, "en")