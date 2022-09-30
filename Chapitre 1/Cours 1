## Sommaire
- [Constantes et variables](#constantes-et-variables)
- [Types](#les-types)
  - [None](#None)
  - [Boolean](#Boolean)
  - [Integer](#Integer)
  - [Float](#Float)
  - String
  - List
  - Dictionary

_____

# Constantes et variables

Dans tous les langages de programmation il est nécessaire de stocker des données, pour les exploiter ou les afficher.

Une **constante** est par définition non modifiable. Elle peut être de tous les **types** possibles.<br>
En python les constantes n'existent pas, si on a besoin d'en utiliser une dans un code conventionnellement son nom est noté en majuscules, pour le différentier des variables.

```python
>>> CONSTANTE = "valeur"
>>> CONSTANTE
"valeur"
```

Une **variable** permet de stocker en mémoire une valeur. En python cette opération est plus simple que dans la plupart des autres langages car l'affectation d'une valeur à une variable utilise le typage dynamique, ce qui veut dire que l'utilisateur n'a pas besoin de renseigner le **type** de la valeur au moment de la création de la variable et l'on peut affecter des valeurs de différents types à une même variable lors de l'exécution du programme.

```python
>>> variable = "ceci est un texte"
>>> variable
"ceci est un texte"
>>> variable = ["ceci","est","une","liste"]
>>> variable
["ceci","est","une","liste"]
```

# Les types

Pour utiliser les constantes et les variables il est nécessaire de savoir travailler avec les types.

> 💡 Il existe de nombreux types différents et de nombreuses bilbiothèques ont leur propre type (les tableaux avec numpy par exemple).

Python comprend 6 types de base qu'il est important de connaître :
+ None
+ Boolean
+ Integer
+ Float
+ String
+ List
+ Dictionaries


## None

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


## Boolean

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


## Integer

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


## Float

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


## String

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


## List

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


## Dict

Les dictionnaires en informatique sont exactement comme les dictionnaires dans la vie réelle. Ils permettent de stocker des "valeurs" indexées avec des "clefs". On les définit avec la syntaxe suivante : `{"clef 1":"valeur 1", "clef 2":"valeur 2"}`.<br>
On peut accéder à une valeur en pointant la clé :
```python
>>> D = {"clef 1":"valeur 1", "clef 2":"valeur 2"}
>>> D["clef 1"]
"valeur 1"
```


# Opérations et méthodes
