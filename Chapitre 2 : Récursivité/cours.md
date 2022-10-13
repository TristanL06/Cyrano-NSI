# Récursivité
## Introduction
Avant d'aborder la récursivité il est primordial de bien différencier un fonction, une procédure et des instructions.

### Des instructions
C'est une suite de commandes, tapées dans l'invite de commande ou écrites à la suite dans l'éditeur de texte. Elles constituent la colonne vertébrale du programme et ne sont exécutées que suivant l'ordre d'écriture.

Par exemple, ces instructions permettent d'ajouter des élèves à une liste :
```python
élève = {}
élève["identite"] = "Alan Turing"
élève["âge"] = 16
élève["taille"] = 1.77
classe.append(élève)
```

Le programme aura bien enregistré les élèves dans la liste `classe` mais si on veut ajouter des élèves depuis plusieurs endroits dans le code il faudra recopier ces 5 lignes. Ça va donc augmenter la difficulté de lecture du code et compliquer la résolution d'erreurs.
___
On va donc utiliser les fonctions et procédures pour simplifier tout ça :
- Une procédure est un objet que l'on peut appeler de n'importe où dans son code en lui donnant des arguments, qui va exécuter du code et **ne rien renvoyer**.
- Une fonction est une procédure qui renvoi quelque-chose. (via `return`)

### Les procédures
Pour reprendre l'exemple de l'élève, on peut définir une procédure `ajout_élève` et l'appeler :
```python
def ajout_élève(prénom, nom, âge, taille):
	élève = {}
	élève["identite"] = prénom + " " + nom
	élève["âge"] = âge
	élève["taille"] = taille
	classe.append(élève)

ajout_élève("Alan", "Turing", 16, 1.77)
```
Ce code donne exactement le même résultat que plus haut mais ajouter un élève prend maintenant une seule ligne claire, beaucoup plus facile à comprendre dans un grand code.

### Les fonctions
Il y a cependant un problème, si on essaye d'exécuter la procédure `ajout_élève("Alan", 5, 16, 1.77)` cela va causer une erreur et arrêter le programme. On peut alors utiliser `try: ... except: ...` pour gérer cette erreur :
```python
def ajout_élève(prénom, nom, âge, taille):
	try:
		élève = {}
		élève["identite"] = prénom + " " + nom
		élève["âge"] = âge
		élève["taille"] = taille
		classe.append(élève)
		return True
	except:
		return False

réussi = ajout_élève("Alan", "Turing", 16, 1.77)
```
On a ici une fonction qui renvoi un booléen, True si l'ajout de l'élève s'est correctement déroulé, False sinon. On peut stocker le retour d'une fonction dans une variable.

## Principe des algorithmes récursifs
Les fonctions récursives fonctionnent en s'appelant elles-même. Pour éviter d'avoir un appel infini de la fonction, surchargeant la mémoire de la machine et devant être interrompue manuellement (`ctrl + c` on rappelle), il est nécessaire d'avoir un **paramètre changeant** et une **condition d'arrêt**.
> :warning: pensez toujours à vérifier que ces deux éléments sont présents lorsque vous travaillez avec les fonctions récursives

Analysons ce code :
```python
def puissance(x, n):
	if n == 0:
		return 1
	return x * puissance(x, n-1)
```
Il permet de calculer $x^n$, en se basant sur le fait que :
$\forall x \not = 0, n > 0 : x^0 = 1$ et $x^n = n \times x^{n-1}$

Si on fait la liste des appels et des retours pour `puissance(2,3)` on obtient :
```txt
appel de puissance(2,3)
	appel de puissance(2,2)
		appel de puissance(2,1)
			appel de puissance(2,0)
				retour de 1
			retour de 2
		retour de 4
	retour de 8
```
Si on suit l'indentation on voit clairement une phase de descente des appels récursifs (tous les appels en cascade) et une phase de remontée (tous les retour). Cela est dû au fait que l'on effectue un calcul sur l'appel de la fonction : __x\*__ puissance(x, n-1).

On peut également représenter ces étapes sous forme de tableau :
|  0  |  1  |  2  |  3  |  4  |  5  |  6  |
| --: | --: | --: | --: | --: | --: | --: |
|     |     |     | **1** 0 |     |     |     |
|     |     |   1 |   1 | **2** 1 |     |     |
|     |   2 |   2 |   2 |   2 | **4** 2 |     |
|   3 |   3 |   3 |   3 |   3 |   3 | **8** 3 |


**Toute notion de fonction terminale et non terminale est hors programme**

\*\* Début du hors programme \*\*

La présence de cette phase de remontée fait que la fonction est **non terminale**.
Pour la rendre **terminale**, la condition d'arrêt doit renvoyer le résultat final. Il faut donc ajouter un argument comme suit :
```python
def puissance(x, n, résultat = 1):
	if n == 0:
		return résultat
	return puissance(x, n-1, x * résultat)
```

Avec cette fonction récursive **terminale** on n'a plus de calcul sur l'appel récursif et la liste des appels ressemble à ça :
```txt
appel de puissance(2,3)
	appel de puissance(2,2,2)
		appel de puissance(2,1,4)
			appel de puissance(2,0,8)
				retour de 8
```
On voit bien qu'il n'y a pas de phase de remontée des appels récurcifs. Pareil avec le tableau :
|  0  |  1  |  2  |  3  |
| --: | --: | --: | --: |
|     |     |     | **8** 0 |
|     |     | **4** 1 |   1 |
|     | **2** 2 |   2 |   2 |
| **1** 3 |   3 |   3 |   3 |

\*\* fin du hors programme \*\*
