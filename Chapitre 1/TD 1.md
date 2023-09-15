# TD 01 : Structures de données


## Exercice 1 : Bases

- Générer une liste des nombres paires entre 2 et 20 inclus.

- Générer la même liste par compréhension

- Grâce à la fonction 'input()' créez un programme demandant à l'utilisateur d'entrer un calcul du type '\<nombre> <opérateur> \<nombre>' (3 \* 4 par exemple) et renvoyant le résultat du calcul. Les opérateurs possibles sont '+', '-', '\*' et '/'.


## Exercice 2 : Jouer avec les fonctions

- Écrire la fonction `mini(L) => int` prenant en entrée une liste d'entiers et retournant le plus petit entier de la liste.

- Faire de même pour la fonction `maxi(L) => int`.

- Mêmes questions, mais la fonction doit renvoyer l'indice du maximum et le maximum dans un tuple.

- Écrire la fonction `générer(int) => L` prenant en entrée un entier et retournant une liste d'entiers qui semblent aléatoires. Pour cette question il est interdit d'utiliser une bibliothèque aléatoire ou pseudo-aléatoire.

- Répéter la question précédente en utilisant la bibliothèque `random`. `from random import randint`

- Écrire la fonction `moyenne(L) => float` prenant en entrée une liste d'entiers et retournant la moyenne de la liste.

- Écrire la fonction `moyenne2(L) => float` prenant en entrée une liste d'entiers et retournant la moyenne de la liste. Cette fois-ci il est interdit d'utiliser la fonction `sum` ou `len`.

- Écrire la fonction `compter_voyelles(str) => int` prenant en entrée une chaîne de caractères et retournant le nombre de voyelles de la chaîne.

- on définit : ```mot = "bonjour"```

	1) Vérifier que **mot** est bien du type *str*
	2) Proposer une fonction prenant en argument un mot de type *str* et renvoyant une liste dont les termes sont les lettres du mot.
	3) Refaites la question 2 avec une autre méthode

- Proposer une fonction prenant pour argument une liste et un nombre et qui renvoie *True* si le nombre est dans la liste, *False* sinon.


## Exercice 3 : Utiliser des fichiers

- Écrire la fonction `lire_fichier(nom_fichier) => str` prenant en entrée le nom d'un fichier et retournant le contenu du fichier sous forme de chaîne de caractères.

- Écrire la fonction `écrire_fichier(nom_fichier, contenu) => None` prenant en entrée le nom d'un fichier et une chaîne de caractères et écrivant le contenu dans le fichier.

- Écrire la fonction `compte_lettres(nom_fichier) => dict` prenant en entrée le nom d'un fichier et retournant un dictionnaire contenant le nombre d'occurrences de chaque lettre dans le fichier. Le dictionnaire doit être de la forme `{'a': 12, 'b': 5, ...}

  

## Exercice 4 : Petits projets

- Jeu de la roue de la fortune. Le programme tire un nombre entier entre 0 et 100. L'utilisateur doit alors entrer un nombre. Si le nombre de l'utilisateur est plus petit que le nombre tiré, le programme affiche 'Plus grand !'. Si le nombre de l'utilisateur est plus grand que le nombre tiré, le programme affiche 'Plus petit !'. Le programme s'arrête lorsque le nombre est trouvé et affiche le nombre de coups nécessaires pour trouver le nombre.

- Jeu du pendu : Le programme tire au hasard un mot de la langue française. L'utilisateur doit alors entrer une lettre. Si la lettre est dans le mot, le programme affiche le mot avec les lettres trouvées. Si la lettre n'est pas dans le mot, le programme affiche un message d'erreur et le nombre de points de l'utilisateur diminue. Le programme s'arrête lorsque le mot est trouvé ou lorsque le nombre de points de l'utilisateur est nul.
