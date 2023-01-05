# TD NSI N°5 : Arbres

## Exercice 1 :
Donner toutes les caractéristiques des arbres suivants, ainsi que les résultats des différentes méthodes de parcours lorsque cela est possible :  
1.  
 ![](https://mermaid.ink/img/pako:eNpNkctuwyAQRX8FTRVpItmbVNl4Vz_SbPqQmk0rNiMbYlRsLMCtKsv_Xr9ow-pc7swFhgFKUwlI4Gqpq9kl5y2b1gPiZb9fOUV8D5whvgTOEV8DF4jnwCfE58C73SPi4T7ILZzFcczSW5FtRy1iu0O2iOJWnP5jSk3O5UIy88mk0jq5O8ojRNAI25CqphcNcxkHX4tGcEgmrISkXnsO0WpJbb7Lmqyf7WHLhrK3X1tDSk45DrMz8nac4vuuIi-KSnljIZGknYiAem_eftoSEm97EYpyRdNQm7DZUfthTPPXJJaMp3X6yyeMvyqWbsI?type=png)

2.  
![](https://mermaid.ink/img/pako:eNpNkcFqhDAQhl8lTC-zoJeFvXisCl66CvViySVoUmWjkRhbivju1ZjsmtP3MZN_QmaBWjUcIvjWbGxJmdCBbOeOeL9cDq4QK885Yu65QCw8l4il5wwx85wgJp5jxPiZcz0FpYipZzeehGFIqrPk7jFWkrMUbpSV-Cz51b3UWupGWynPkr1m15JNU8IFUQ8iOimjt5u4QQA91z3rmu2jlr2Ngml5zylEGzZcsFkaCsFRElL91i3TZi8vLhvqWf-4C-9s6iYKe2Wlw7rFz2PDDE-bzigNkWBy4gGw2ajPv6GGyOiZ-6akY9uu-mfXyIYvpV7ObcjHsVW73PUfd4WB2w?type=png)

3.  
![](https://mermaid.ink/img/pako:eNpNkUtvgzAQhP-Ktb1s1HAoag7l2FApl5ZI5ZLKlxXYBdVgZEwfQvz38rAT-zSfZndG8o5Q6FJAAp-GuorlKW_Z_N4Qf3e7TWeI915fEDlEHDzniI9enxBjr8-IT16nwf4R8eGaGwfgalkURSwL4eKKV0hDOLv4FY4hZLFrWCkP4XSrKxT1fSok019M1koldwd5gD00wjRUl_OfjMsYB1uJRnBIZlkKSYOyHPabJZX-KSoydrFHlw3FYL7dwjP1dc9hcSbeTnP80JVkxUtZW20gkaR6sQcarH7_awtIrBmEH0prms_SXKc6aj-0vrFYQ163A653nP4BcR58_w?type=png)

4.  
![](https://mermaid.ink/img/pako:eNpNkUFrhDAQhf-KTC-zoNDaWorHXYW9tC7UyxYvQZMqjUZibCnif2-MSTc5vY-ZN2_ILFCLhkIKn5KMbVBm1RDo94b4cH847HBFfHG6QHxy-oL47HSJGDt91manM8TE6ZPnLWLPkCM-Om3zgyiKgqsPhV3GQObDxUYZOPlQxHZTQ7mNNlD6cL5l15xMU0ZZIL4C1nGe3iUsgRB6KnvSNfqnlq2tAtXSnlaQatlQRmauKgj3EuPip26JVFt5sbOhnuW3NRzJ1E0VbJW1GlY9fh4bomjedEpISBnhEw2BzEq8_w41pErO1DVlHdHH6v-7RjJ8CHFjaoa87mc1113_AEX4gRI?type=png)


### Exercice 2 : Travail avec des tuples

On implémente les arbres binaires non vides par des tuples de trois éléments : `(valeur,(fils gauche),(fils droit)]`. Écrivez les fonctions suivantes en  Python :
1. `est_vide(arbre)` qui retourne `True` si l'arbre est vide, `False` sinon
2. `fils_gauche(arbre)` qui retourne le fils gauche de **a** si a est non vide, `None` sinon.
3. `fils_gauche(arbre)` qui retourne le fils gauche de **a** si a est non vide, `None` sinon.
4. `afficher(arbre, mode)` qui affiche les valeurs de l'arbre selon le mode précisé (`profondeur`, `préfixe`, `infixe`, `postfixe`).
5. `recherche_iter(valeur, arbre)` qui retourne si la valeur est présente dans l'arbre, de manière itérative.
6. `recherche_rec(valeur, arbre)` qui fait la même chose que `recherche_iter`, mais de manière récursive.
7. `hauteur(arbre)` retourne la hauteur de l'arbre
8. `taille(arbre)` retourne la taille de l'arbre


### Exercice 3 : Un peu de POO c'est rigolo (et surtout plus facile de travailler avec un objet)

- Écrire la classe `arbreBinaire` contenant toutes les méthodes et tous les attributs que vous jugez utiles.
- Modifiez les méthodes `prefixe`, `infixe` et `suffixe` de la classe fournie ([ressources](https://github.com/TristanL06/Cyrano-NSI/blob/main/Chapitre%205%20:%20Arbres%20binaires/ressources/arbres.py)) pour qu'elles n'affichent plus les étiquettes mais qu'elles les renvoient sous forme d'une liste.


### Exercice 4 : Arbres binaires de recherche

- Écrire un arbre binaire de recherche de taille 5 et de profondeur 2
- Ajouter deux valeurs à cet arbre
- Quelle est sa taille ? Sa profondeur ?
- Créez-le avec la classe construite dans l'exercice 3 (une [proposition de correction](https://github.com/TristanL06/Cyrano-NSI/blob/main/Chapitre%205%20:%20Arbres%20binaires/ressources/arbres.py) est disponible)
- Parcourez l'objet créé avec les méthodes de parcours en profondeur. Que remarquez-vous ?
