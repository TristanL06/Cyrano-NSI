# Exercice 1
1) Écrire une fonction prenant en paramètre une liste de nombres et retournant leur somme
2) Faire de même pour leur produit (multiplication)
3) Écrire une fonction prenant deux listes en argument et renvoyant un booléen évalué à Vrai si il y a au moins un élément en commun aux deux listes.
4) Créer une fonction **nombreOccurences()** qui prend une liste L et un élément x comme paramètres et qui retourne le nombre de fois où l’élément x apparait dans la liste L (sans utiliser la fonction **count()** ).
5) Créer une fonction **InsertEtoile()**  qui place  des "étoiles " entre chaque caractères d'une chaine fournie en entrée. **Exemple** pour la chaine s = "Python" , **InsertEtoile(s)** donne **P\*t\*h\*o\*n**
6) Créer une fonction **toutEnMajuscule()** qui permet de transformer une liste de chaines en une autre liste constituée de chaines en majuscule. On rappelle que pour passer une chaine de caractère en majuscule on utilise la méthode `upper()` : `"coucou".upper() => 'COUCOU'`
7) Écrire une fonction qui prends en argument une chaine de caractères **s** et qui renvoie le nombre de minuscules et de majuscules contenu dans la chaine **s**.
8) Écrire une fonction qui prends en paramètre une liste de  nombres entiers et qui renvoie un dictionnaire dont les clés sont les entiers de la liste et dont les valeurs sont 'pair' ou 'impair' selon la parité du nombre.

## Exercice 2
1) Écrire une fonction renvoyant la liste des chiffres d'un nombre écrit en base 10 en utilisant uniquement les opérateurs numériques.
2) Écrire une **fonction** qui prends en arguments  **deux nombres entiers a  et  b**   et qui renvoie un tuple formé de :
	1) Le **quotient q** de la **division euclidienne** de **a** par **b** (sans utiliser l'**opérateur //** )
	2) Le **reste r** de la division euclidienne de **a** par **b** (sans utiliser l'**opérateur %** )
3) Écrire une **fonction** qui prends en arguments  **deux nombres entiers a  et  b**   et qui renvoie le PGCD de  **a** et **b** sans utiliser aucune fonction prédéfinie en python.
4) Écrire une **fonction** qui prends en arguments  **deux nombres entiers a  et  b**   et qui renvoie le PPCM de  **a** et **b** sans utiliser aucune fonction prédéfinie en python.
5) Écrire une **fonction** qui prends en argument un **entier n** et qui renvoie **True** si l'entier **n est premier** et **False si non**.
6) Écrire une fonction qui prends **deux nombres m et n en** paramètres (**m<n**) et qui renvoie une **liste** formée de tous  les **nombres premiers compris entre m et n**. Exemple pour **m=10** et **n=20** la fonction doit renvoyer **[11 , 13 , 17 , 19]**
7) Écrire une fonction qui prends en argument deux nombres entiers **a**  et  **b**   et lui renvoie **True** si les nombres sont premiers entre eux et **False** si non.


# TP Développement d'une calculatrice
Dans ce TP, nous allons explorer deux concepts fondamentaux liés au développement d'une calculatrice : la Notation Polonaise Inverse (NPI) et l'Algorithme de Shunting-yard. Ces deux techniques sont essentielles pour créer un système de calcul efficace et polyvalent.

## Exercice préalable :
Dans la suite nous aurons besoin d'utiliser des piles et des files.
Écrivez les classes correspondantes comportant les méthodes :
- empile (resp. enfile)
- depile (resp. defile)
- estVide
- sommet
en respectant les principes des piles et files.

## 1 : Notation Polonaise Inverse
La notation polonaise inverse permet de représenter les expressions mathématiques de manière optimisée afin de les traiter facilement. Elle diffère de la notation traditionnelle (infixe) en plaçant les opérateurs après leurs opérandes, ce qui élimine la nécessité d'utiliser des parenthèses pour indiquer l'ordre d'évaluation.
Au lieu de représenter `5 + 3` on note `5 3 +`, de même `(4 + 6) * (7 + 8)` sera noté `4 6 + 7 8 + *`

Pour calculer le résultat d'une expression en NPI on va utiliser une pile et suivre les étapes suivantes :
- Si on traite un nombre on l'empile
- Si on traite un symbole, on dépile les deux derniers nombres de la pile, on applique l'opération (en faisant attention à l'ordre) et on empile le résultat. 

À la fin de l'exécution on doit avoir une seul valeur dans la pile, correspondant au résultat du calcul.


## 2 : Algorithme de Shunting-yard
La façon de traiter les opérations nécessite d'avoir une NPI, ce qui n'est pas trivial. Il faut donc utiliser un algorithme pour transformer une notation traditionnelle ( 4 + 2 par exemple) en NPI ( 4 2 + ).
C'est le but de l'algorithme de Shunting-Yard.
Cet algorithme utilise la priorité des opérations (la puissance (\*\*) est prioritaire sur la multiplication/division etc...) et les parenthèses pour transformer les opérations mathématiques de la notation traditionnelle vers la NPI.

- En cherchant sur internet et dans toutes les ressources à disposition expliquez les étapes de fonctionnement de l'algorithme de shunting-yard. Écrire l'algorithme en python. 
- Faire une courte présentation pour expliquer l'algoithme ainsi créé.


## Annexes
### Quelques notations polonaises inverses :
**Example 1: Addition**

NPI: 5 3 +
Mathematics: 5 + 3
Result: 8

**Example 2: Subtraction**

NPI: 7 2 -
Mathematics: 7 - 2
Result: 5

**Example 3: Multiplication**

NPI: 4 6 *
Mathematics: 4 * 6
Result: 24

**Example 4: Division**

NPI: 8 2 /
Mathematics: 8 / 2
Result: 4

**Example 5: More Complex Expression**

NPI: 3 4 + 5 6 * -
Mathematics: (3 + 4) - (5 * 6)
Result: -17

**Example 6: Using Parentheses**

NPI: 3 4 + 5 6 * - 2 /
Mathematics: ((3 + 4) - (5 * 6)) / 2
Result: -8
