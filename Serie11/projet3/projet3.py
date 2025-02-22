import requests
import random
import json

def recuperer_questions(nombre: int, difficulte: str = "easy", langue: str = "en"):
    url = f"https://opentdb.com/api.php?amount={nombre}&difficulty={difficulte}&type=multiple&encode=url3986"
    response = requests.get(url)
    data = response.json()
    return data["results"]

def jouer_quiz(questions, langue="en"):
    score = 0
    for question in questions:
        q = requests.utils.unquote(question["question"])
        print("\n" + q)
        reponses = [requests.utils.unquote(question["correct_answer"])] + \
                   [requests.utils.unquote(r) for r in question["incorrect_answers"]]
        random.shuffle(reponses)
        for i, reponse in enumerate(reponses, 1):
            print(f"{i}. {reponse}")
        
        choix = int(input("Votre réponse (numéro) : "))
        if reponses[choix - 1] == requests.utils.unquote(question["correct_answer"]):
            print("Correct !" if langue == "en" else "Correct !")
            score += 1
        else:
            print(f"Faux ! La réponse correcte était : {requests.utils.unquote(question['correct_answer'])}")

    print(f"\nScore final : {score}/{len(questions)}")

def menu_quiz():
    while True:
        print("\nQuiz Game :")
        print("1. Jouer")
        print("2. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            nombre = int(input("Nombre de questions : "))
            difficulte = input("Difficulté (easy/medium/hard) : ")
            langue = input("Langue (en/fr) : ")
            questions = recuperer_questions(nombre, difficulte, langue)
            jouer_quiz(questions, langue)
        elif choix == "2":
            print("Au revoir !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    menu_quiz()