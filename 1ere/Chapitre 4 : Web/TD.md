# Chapitre 4 : Les langages WEB

# Exercice 1 : Créer une page avec une recette de cuisine
1) Écrire le code HTML pour créer la structure d'une page web comme montré dans le cours.
2) Ajouter le titre de la recette, le temps de préparation, le coût, la difficulté et le nombre de personnes.
3) Ajouter la liste des ingrédients (liste non ordonnée)
4) Ajouter la liste des étapes (liste ordonnée)
5) Ajouter une image de la recette
6) Ajouter un lien vers une page web qui contient une autre recette
7) Modifier le titre de la page web, ainsi que l'icône, qui s'affichent dans l'onglet du navigateur.

# Exercice 2 : Mettre en page la page web créée dans l'exercice 1
1) Créer un fichier CSS et le lier à la page web.
2) Modifier la couleur des titres et des textes
3) Modifier la couleur du fond de la page
4) Modifier la taille de l'image de la recette

# Exercice 3 : Jouer avec flask
1) Créer un fichier `app.py` et écrire le code suivant :
```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"message": "pong!"})
```
2) En utilisant les paramètre, créez une route qui calcul la somme de deux nombres.
3) En utilisant les paramètre, créez une route qui calcul la différence de deux nombres.
4) En utilisant les paramètre, créez une route qui calcul le produit de deux nombres.
5) En utilisant les paramètre, créez une route qui calcul le quotient de deux nombres.

# Projet : Créer un site web de contenu vidéo
