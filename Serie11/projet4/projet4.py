import speech_recognition as sr
from gtts import gTTS
import os

regles = {
    "bonjour": "Bonjour ! Comment puis-je vous aider aujourd'hui ?",
    "au revoir": "Au revoir ! À bientôt.",
    "default": "Désolé, je ne comprends pas."
}

def ecouter():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Je vous écoute...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language="fr-FR")
        except:
            return "incompréhensible"

def parler(message):
    tts = gTTS(text=message, lang="fr")
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

def chatbot():
    print("Bienvenue ! Parlez 'au revoir' pour quitter.")
    while True:
        message = ecouter().lower()
        print(f"Vous : {message}")
        if "au revoir" in message:
            parler(regles["au revoir"])
            break
        elif message in regles:
            parler(regles[message])
        else:
            parler(regles["default"])

if __name__ == "__main__":
    chatbot()