Introduction / Rappel à la programmation python

# Introduction

## Interface

Le principal langage sur lequel nous allons nous baser est **Python**, il est donc important de savoir comment l'utiliser.
Sous Spyder (de même que sur la plupart des IDE) il y a deux éléments primordiaux : l'**éditeur** et l'**interpréteur**.
![Interface Spyder](https://assets.lls.fr/pages/35776949/capture-d-cran-2020-10-29-095757.png)

Pour tester simplement une commande on peut utiliser l'interpréteur, pas besoin d'utiliser la fonction `print` pour avoir un retour du résultat.
> C'est pratique pratique pour tester les fonctions mais totalement inadapté pour un code complet

C'est pour ça que l'on va écrire dans l'éditeur de texte. On va pouvoir y mettre un programme complet et l'*exécuter* en appuyant sur le triangle vert (ou `f5`). Le résultat sera affiché dans l'interpréteur.
> :warning: Si la foction *print()* n'est pas utilisée le programme va bien s'exécuter mais ne va rien renvoyer

___
## Constantes et variables

Dans tous les langages de programmation il est nécessaire de stocker des données, pour les exploiter ou les afficher.

Une **constante** est par définition non modifiable. Elle peut être de tous les **types** possibles.<br>
En python les constantes n'existent pas, si on a besoin d'en utiliser une dans un code conventionnellement son nom est noté en majuscules, pour le différentier des variables.

```python
>>> CONSTANTE = "valeur"
>>> CONSTANTE
"valeur"
```
*Ici on **affecte** la valeur "valeur" à la variable **CONSTANTE***

Une **variable** permet de stocker en mémoire une valeur. En python cette opération est plus simple que dans la plupart des autres langages car l'affectation d'une valeur à une variable utilise le typage dynamique, ce qui veut dire que l'utilisateur n'a pas besoin de renseigner le **type** de la valeur au moment de la création de la variable et l'on peut affecter des valeurs de différents types à une même variable lors de l'exécution du programme.

```python
>>> variable = "ceci est un texte"
>>> variable
"ceci est un texte"
>>> variable = ["ceci","est","une","liste"]
>>> variable
["ceci","est","une","liste"]
```
___
## Les types

Pour utiliser les constantes et les variables il est nécessaire de savoir travailler avec les types.

> 💡 Il existe de nombreux types différents et de nombreuses bilbiothèques ont leur propre type (les tableaux avec numpy par exemple).

Python comprend 6 types de base qu'il est important de connaître :
- [None](#None)
- [Boolean](#Boolean)
- [Integer](#Integer)
- [Float](#Float)
- [String](#String)
- [List](#List)
- [Dictionary](#Dict)



### None

None est un type très particulier de python, qui ne contient que l'objet None. Il n'est égal qu'à lui-même et est la réponse renvoyée par défaut par toutes les fonctions se terminant sans `return`

```python
>>> None
None
>>> type(None)
<class 'NoneType'>
>>> None == None
True
```

En pratique il est rarement utilisé et toujours dans des cas assez simples. Il faut donc juste savoir qu'il existe.


### Boolean

Boolean (Booléen en français) est LE type du binaire.

Un booléen peut prendre exactement 2 valeurs : 0 et 1<br>
Le 0 est également appelé False et le 1 est appelé True.

Plusieurs booléens forment des nombres binaires, qui sont à la base du fonctionnement de tous les appareils électroniques.

Les booléens peuvent êtres comparés les uns aux autres par les comparateurs `>` ; `>=` ; `<` ; `<=` ; `==` ; `!=`<br>
La seule méthode qu'on peut lui appliquer est le `not`, qui permet de changer sa valeur :
```python
>>> etat = True
>>> etat = not etat
>>> etat
False
```

La fonction `bool()` permet de retourner un booléen en prenant en argument n'importe quel objet.<br>
Si l'objet est un nombre (type numérique), `bool()` renvoie `False` si il est égale à 0, il renvoie `True` sinon :
```python
>>> bool(0)
False
>>> bool(1)
True
>>> bool(3)
True
>>> bool(0.0)
False
```

Pour tous les autres types, si la taille est nulle (liste vide, tuple vide, chaine de caractère vide ou dictionnaire vide) elle renvoie `False`, elle renvoie `True` sinon.

```python
>>> bool("")
False
>>> bool("chaine de caractères")
True
>>> bool([])
False
```
Avec `None` ça retourne toujours `False`


### Integer

Ce type regroupe tous les entiers relatifs ( comme -1, 0, 1, 2...). Contrairement à d'autres langages (comme le C ou JavaScript), il n'est pas nécessaire de s'occuper de la taille des entiers stockés, python gère tout seul en fonction de la place nécessaire.

Une cours spécifique va arriver mais vous pouvez juste retenir que :
+ On peut stocker tous les nombres de 0 à 255 (256 nombres) sur 1 octet (8 bits)
+ On peut stocker tous les nombres de -128 à 127 (256 nombres) sur 1 octet (8 bits)

Des opérations mathématiques peuvent être appliquées sur les entiers : <br>
+ L'addition : `+`
```python
>>> 2 + 3
5
```
+ La soustraction : `-`
```python
>>> 2 - 3
-1
```
On peut également utiliser la division (`/`), la multiplication (`*`) et de nombreux autres.


### Float

Les flottants (float) regroupent tous les nombres décimaux : `3.5` ou `4.21` par exemple.<br>
Ils sont écrits selon la norme anglo-saxonne, donc avec un point à la place de la virgule.<br>
> ⚠️La méthode informatique utilisée pour le stockage des flottants les approximent très légèrement. Il est donc très fortement déconseillé d'utiliser des égalités strictes (`==`,`!=`)

Les même opérations mathématiques que pour les entiers peuvent être utilisées.<br>
Elles peuvent être utilisées entre des entiers et des flottants :
```python
>>> 3.5 * 6
21.
>>> 1.25 * 5
6.25
```

Le nombre `5.` est égale à 5 mais stocké sous forme flottant, ce qui explique la présence du point à la fin.


### String

Les chaines de caractère sont des suites de caractères qui peuvent contenir des lettres, des chiffres, des signes...<br>
ils sont représentés entre deux guillemets (`'chaine de caractères'`), deux double guillemets (`"chaine de caractères"`), ce qui est strictement équivalent.

On peut appliquer de nombreuses opérations à des chaines de caractère comme la concaténation (`+`) ou la multiplication (`*`). Il est également possible de sélectionner un ou plusieurs caractères dans une plage :
```python
>>> a = "ceci est mon string"
>>> a
"ceci est mon string"
>>> a = a + " Python"
>>> a
"ceci est mon string Python"
>>> a[3]
"i"
>>> a[5:8]
"est"
```


### List

Une liste peut contenir des éléments de n'importe quel type. On peut ajouter (`L.append()`,`L.instert()`), enlever (`L.pop()`) un élément à une liste, concaténer deux listes ensemble  et accéder aux éléments d'une liste avec leur indexe.
```python
>>> L = ["salut", "ceci", "est", 1, ["liste"]]
>>> L.append("pleine")
>>> L
["salut", "ceci", "est", 1, ["liste"], "pleine"]
>>> "est" in L
True
>>> "liste" in L
False
>>> len(L)
6
```

> ⚠️ Lorsque l'on utilise `P = L`, les deux variables L et P pointent vers le même objet. Toute modification sur l'une des deux listes est répercutée sur l'autre. Il faut utiliser `P = L[:]` ou `P = copy.deepcopy(L)` pour éviter cela.

> 💡 Les tuples sont des objets similaires aux listes, mais non modifiables

Il est possible de créer des listes par compréhension qui remplace
```python
L = []
for i in range(10):
	L.append(i)
```
par
```python
L = [i for i in range(10)]
```

### Dict

Les dictionnaires en informatique sont exactement comme les dictionnaires dans la vie réelle. Ils permettent de stocker des "valeurs" indexées avec des "clefs". On les définit avec la syntaxe suivante : `{"clef 1":"valeur 1", "clef 2":"valeur 2"}`.<br>
On peut accéder à une valeur en pointant la clé :
```python
>>> D = {"clef 1":"valeur 1", "clef 2":"valeur 2"}
>>> D["clef 1"]
"valeur 1"
```
Pour modifier une valeur associée à une clé il suffit de la réassigner comme ceci :
```python
>>> D["clef 1"] = "valeur a"
>>> D
{"clef 1":"valeur a", "clef 2":"valeur 2"}
```
On peut récupérer toutes les clefs d'un dictionnaire avec la méthode `D.keys()`
___
## Opérations sur les variables
### Tests
Les tests permettent de comparer deux valeurs de même type. Un test renverra toujours un résultat [Booléen](#Boolean) (True ou False).

| Test | Console | Utilisation | Résultat | Type | Question posée |
| :-------: | :---: | :-: | :-------: | :---: | - |
| = | == | 20 == 3 | False | bool | Est-ce que 20 = 3 ? |
| $\neq$ | != | 20 != 3 | True | bool | Est-ce que 20 $\neq$ 3 ? |
| < | == | 20 < 3 | False | bool | Est-ce que 20 < 3 ? |
| $\leqslant$ | <= | 20 <= 3 | False | bool | Est-ce que 20 $\leqslant$ 3 ? |
| > | > | 20 > 3 | True | bool | Est-ce que 20 > 3 ? |
| $\geqslant$ | >= | 20 >= 3 | True | bool | Est-ce que 20 $\geqslant$ 3 ? |
___
### Claculs sur les nombres
Un ordinateur est capable d’effectuer différentes opérations mathématiques avec des nombres entiers et décimaux mais également avec d’autres types de données comme des chaînes de caractères.  
  
L’ensemble des exemples présentés par la suite sont à saisir dans la console Python. Pour en afficher le résultat, on utilise la fonction **print()**.  
  
Le type caractérise la nature de la valeur : il peut s’agir d’un nombre entier , d’un nombre en virgule flottante, d’une chaîne de caractères ou d’un booléen.

| Opérateur | Console | Utilisation | Résultat | Type | Explication |
| :-------: | :---: | :-: | :-------: | :---: | - |
| + | + | 20 + 3 | 23 | int | Addition de 20 et 3 |
| - | - | 20 - 3 | 17 | int | Soustraction de 20 et 3 |
| x | * | 20 * 3 | 60 | int | Multiplication de 20 et 3 |
| % | / | 20 / 3 | 6.66667 | float | Division de 20 et 3 |
|  | // | 20 // 3 | 6 | int | Partie entière de la division euclidienne de 20 par 3 |
| modulo | % | 20 % 3 | 2 | int | Reste de la division euclidienne de 20 par 3 |
| ^ (puissance) | ** | 2 ** 3 | 8 | int | 2 puissance 3 |

#### Opérateurs d'affectation
Les opérateurs d'affectation sont utilisés en **Python** pour rendre le code plus aéré et lisible. Il consiste à remplacer la modification classique d'une variable par un affectation plus compacte.

| modification classique | Opérateurs d'affectation |
| :-: | :-: |
| a = a + 3 | a += 3 |
| a = a - 3 | a -= 3 |
| a = a * 3 | a \*= 3 |
| a = a / 3 | a /= 3 |
| a = a // 3 | a //= 3 |
| a = a % 3 | a %= 3 |
| a = a ** 3 | a \*\*= 3 |
___
### Opérations sur les chaines de caractères
On peut utiliser un + entre deux chaines de caractères pour les mettre à la suite :
```python
>> a = 'Cours '
>> b = 'Cyrano'
>> c = a + b
>> print(c)
'Cours Cyrano'
```
> 💡 la chaine de caractère *a* se termine par un espace

on peut aussi utiliser le signe \* pour répéter un certain nombre de fois une chaine de caractères :
```python
>> 'cous' * 2
'couscous'
```
___

## Boucles et conditions

On sait maintenant travailler sur des variables, leur associer des valeurs, les convertir et faire des calculs avec.
Pour créer des programmes il ne reste plus qu'à répéter ces action et c'est là qu'interviennent les boucles.

Il existe deux types de boucles, les boucles **while** et les boucles **for**. La boucle while s'exécute tant que sa **condition** est vrai (Booléen True). La boucle for s'exécute pour un nombre d'itérations **connues à l'avance**.

Dans les deux cas l'**indentation** est primordiale !
Tout le code indenté (décalé d'un cran vers la droite avec la touche tab) sera exécuté dans la boucle, il faut redescendre l'indentation pour sortir de la boucle.

### La boucle while
La boucle while prend en argument une condition et exécute le code tant que cette condition est vraie (True : Boolean)
```python
while(condition):
	code à exécuter dans la boucle
code hors de la boucle
```

> :warning: Si la condition est toujours vrai cela génère une boucle infinie. Pour éviter la surchauffe de votre PC. On peut utiliser la commande `ctrl+c` pour interrompre le processus.

```
i = 0
while i < 3:
	print(i)
	i += 1
```
```python
0
1
2
```
> :warning: oublier la ligne `i += 1` va faire que i < 3 sera toujours vrai et génèrera donc une boucle infinie

___
### La boucle for
La boucle *for* permet de parcourir un objet.

En l'utilisant avec `range(D,F,P)` cela va parcourir l'intervalle de D à F (exclu) par pas de P :
> range(1,6,2) va générer l'intervalle comprenant [1, 3, 5]

```python
for i in range(4):
	print(i)
```
```python
0
1
2
3
```

Si l'objet est une liste elle va être parcourue et la variable va prendre la valeur des éléments de cette liste tour-à-tour :
```python
for element in ['a','b','c','d']:
	print(element)
```
```python
'a'
'b'
'c'
'd'
```
 et cela fonctionne exactement de la même manière avec une chaine de caractères :
```python
for element in ["abcd"]:
	print(element)
```
```python
'a'
'b'
'c'
'd'
```
___
### Les conditions (if)

les conditions permettent d'exécuter un code en fonctiondu résultat d'un test. Elle se définie avec une ligne commençant par **if**, se terminant avec `:` et comportant un test :
```python
a = 4
if a > 3:
	print("a est strictement supérieur à 3")
```
```python
"a est strictement supérieur à 3"
```

Dans cet exemple on test si notre variable a est supérieur à 3. Le test `a > 3` renvoie `True`, la condition étant vraie ce qui est indenté s'exécute. On peut ajouter un **else** qui s'exécute si la condition est fausse :
```python
a = 4
if a > 3:
	print("a est strictement supérieur à 3")
else:
	print("a n'est pas strictement supérieur à 3")
```
ici on peut traduire tout ça en français :
*Si a est strictement supérieur à 3, on affiche la première phrase, sinon on affiche la seconde phrase*

Il existe un dernier mot-clé : `elif`, qui est la contraction de *else* et *if*
Il permet de ne pas imbriquer de nombreuses conditions.

Voici quelque-chose à ne pas faire :
```python
if a > 3:
	print("a est strictement supérieur à 3")
else:
	if a < 0:
		print("a est un nombre négatif")
	else:
		print("a est compris entre 0 et 3 inclus")
```

il faut préférer écrire :
```python
if a > 3:
	print("a est strictement supérieur à 3")
elif a < 0:
	print("a est un nombre négatif")
else:
	print("a est compris entre 0 et 3 inclus")
```
Ici on peut traduire ça par :
*Si a est strictement supérieur à 3, on affiche la première phrase, sinon si a est strictement inférieu à 0 on affiche la deuxième phrase sinon on affiche la troisième phrase*

> :warning: Il est primordiale de faire très attention aux indentations pour les boucles et les conditions, c'est l'une des plus grande source d'erreurs, avec l'oublie des ':' et l'utilisation du '=\='

### Les instructions

C'est une suite de commandes, tapées dans l'invite de commande ou écrites à la suite dans l'éditeur de texte. Elles constituent la colonne vertébrale du programme et ne sont exécutées que suivant l'ordre d'écriture.

Par exemple, ces instructions permettent d'ajouter des élèves à une liste classe :

```python
élève = {}
élève["identite"] = "Alan Turing"
élève["âge"] = 16
élève["taille"] = 1.77
classe.append(élève)
```

Le programme aura bien enregistré les élèves dans la liste `classe` mais si on veut ajouter des élèves depuis plusieurs endroits dans le code il faudra recopier ces 5 lignes. Ça va donc augmenter la difficulté de lecture du code et compliquer la résolution d'erreurs.

---

On va donc utiliser les fonctions et procédures pour simplifier tout ça :

-   Une procédure est un objet que l'on peut appeler de n'importe où dans son code en lui donnant des arguments, qui va exécuter du code et **ne rien renvoyer**.
-   Une fonction est une procédure qui renvoi quelque-chose. (via `return`)

### Les procédures

Pour reprendre l'exemple de l'élève, on peut définir une procédure `ajout_élève` et l'appeler :

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

Il y a cependant un problème, si on essaye d'exécuter la procédure `ajout_élève("Alan", 5, 16, 1.77)` cela va causer une erreur et arrêter le programme. On peut alors utiliser `try: ... except: ...` pour gérer cette erreur :

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
