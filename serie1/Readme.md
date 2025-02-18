### **Mini README : Bonnes pratiques et erreurs à éviter pour les bases de Python**

---

#### **Bonnes pratiques à adopter :**
1. **Noms de variables explicites :**
   - Utilisez des noms significatifs pour vos variables (ex. `longueur`, `largeur` au lieu de `l` ou `x`).
   - Respectez la convention de nommage en minuscules avec des underscores (`snake_case`) pour les variables.

2. **Typage explicite :**
   - Convertissez explicitement les types de données lorsque nécessaire (ex. `int()` ou `float()` pour les entrées utilisateur).

3. **Gestion des erreurs :**
   - Utilisez des blocs `try-except` pour gérer les exceptions, notamment lors de l'entrée utilisateur.
   - Validez les données d'entrée pour éviter des calculs incorrects (ex. vérifiez que les dimensions sont positives).

4. **Utilisation des f-strings :**
   - Préférez les f-strings pour formater les chaînes de caractères plutôt que la concaténation avec `+`.

5. **Code modulaire et lisible :**
   - Structurez votre code pour qu'il soit facile à lire et à comprendre.
   - Ajoutez des commentaires pour expliquer les sections complexes ou importantes.

6. **Tests unitaires implicites :**
   - Testez votre code avec différentes valeurs pour vous assurer qu'il fonctionne dans tous les cas possibles.

---

#### **Erreurs courantes à éviter :**

1. **Entrées utilisateur non validées :**
   - Ne pas convertir correctement les entrées utilisateur en types appropriés (ex. `input()` renvoie toujours une chaîne).
   - Ne pas vérifier que les valeurs entrées sont positives ou respectent les contraintes du problème.

2. **Confusion entre types de données :**
   - Tenter d'effectuer des opérations mathématiques sur des chaînes de caractères sans conversion préalable.
   - Oublier que certaines fonctions comme `input()` renvoient des chaînes par défaut.

3. **Absence de gestion des erreurs :**
   - Ne pas anticiper les erreurs potentielles (ex. division par zéro, conversion impossible).

4. **Nom de variables inappropriés :**
   - Utiliser des noms courts ou ambigus qui rendent le code difficile à comprendre.
   - Utiliser des noms réservés par Python comme variables (ex. `list`, `str`, `int`).

5. **Manque de formatage :**
   - Ne pas utiliser les f-strings ou des méthodes similaires pour formater les chaînes de manière claire.

6. **Code répétitif :**
   - Répéter des portions de code au lieu de les factoriser dans des fonctions ou des boucles.

---

### **Barème pour la série (sur 100 points) :**

#### **Partie 1 : Déclaration et affichage de variables (15 points)**
- Variable déclarée correctement avec un nom explicite : **5 points**
- Affichage correct de la variable : **5 points**
- Code bien structuré et lisible : **5 points**

#### **Partie 2 : Formatage avec f-string (20 points)**
- Trois variables créées avec des noms explicites : **5 points**
- Utilisation correcte de f-strings pour afficher les variables : **10 points**
- Code propre et bien commenté : **5 points**

#### **Partie 3 : Somme de deux nombres (20 points)**
- Demande correcte de deux nombres à l'utilisateur : **5 points**
- Conversion des entrées en type numérique (`float` ou `int`) : **5 points**
- Calcul et affichage corrects de la somme : **5 points**
- Gestion des erreurs avec `try-except` : **5 points**

#### **Partie 4 : Conversion entre types (15 points)**
- Conversion d'un entier en chaîne de caractères : **5 points**
- Conversion inverse d'une chaîne en entier : **5 points**
- Code bien documenté et sans erreurs : **5 points**

#### **Partie 5 : Calcul de l'aire d'un rectangle (30 points)**
- Demande correcte de longueur et largeur à l'utilisateur : **5 points**
- Validation des entrées (positivité des dimensions) : **10 points**
- Calcul correct de l'aire : **5 points**
- Gestion des erreurs avec `try-except` : **5 points**
- Affichage clair avec f-strings : **5 points**

---

#### **Total : 100 points**

---

### **Conseils supplémentaires :**
- Prenez le temps de tester votre code avec différents scénarios pour vous assurer qu'il est robuste.
- Relisez votre code pour vérifier qu'il respecte les bonnes pratiques mentionnées ci-dessus.
- N'hésitez pas à demander de l'aide si vous rencontrez des difficultés !