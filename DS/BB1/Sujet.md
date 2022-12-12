# Bac Blanc de NSI

### 06/12/2022
---

### Le sujet est à traiter en 4h
  
### Toute trace de recherche sera prise en compte.  

### Le candidat devra rendre ses réponses sur feuilles numérotées (x/max) à la fin du temps prévu.


___
## Exercice 1 (BAC 2021 centres étrangers 1)
#### *Notion abordée : structures de données (dictionnaires)*

Une ville souhaite gérer son parc de vélos en location partagée. L’ensemble de la flotte de vélos est stocké dans une table de données représentée en langage Python par un dictionnaire contenant des associations de type `id_velo` : `dict_velo` où `id_velo` est un nombre entier compris entre 1 et 199 qui correspond à l'identifiant unique du vélo et `dict_velo` est un dictionnaire dont les clés sont : "type", "etat", "station".

Les valeurs associées aux clés "type", "etat", "station" de dict_velo sont de type chaînes de caractères ou nombre entier :
- "type" : chaîne de caractères qui peut prendre la valeur "electrique" ou "classique"
- "état" : nombre entier qui peut prendre la valeur 1 si le vélo est disponible, 0 si le vélo est en déplacement, -1 si le vélo est en panne
- "station" : chaînes de caractères qui identifie la station où est garé le vélo.

Dans le cas où le vélo est en déplacement ou en panne, "station" correspond à celle où il a été dernièrement stationné.  
Voici un extrait de la table de données :

```txt
flotte = {
   12 : {"type" : "electrique", "etat" : 1, "station" : "Jean Médecin"},
   80 : {"type" : "classique", "etat" : 0, "station" : "Les Eucalyptus"},
   45 : {"type" : "classique", "etat" : 1, "station" : "Ferber"},
   41 : {"type" : "classique", "etat" : -1, "station" : "CADAM"},
   26 : {"type" : "classique", "etat" : 1, "station" : "Palais Nikaïa"},
   28 : {"type" : "electrique", "etat" : 0, "station" : "Palais Nikaïa"},
   74 : {"type" : "electrique", "etat" : 1, "station" : "Lanval"},
   13 : {"type" : "classique", "etat" : 0, "station" : "CADAM"},
   83 : {"type" : "classique", "etat" : -1, "station" : "Les Eucalyptus"},
   22 : {"type" : "electrique", "etat" : -1, "station" : "Ferber"}
}
```

`flotte` étant une variable globale du programme.

Toutes les questions de cet exercice se réfèrent à l'extrait de la table `flotte` fourni ci-dessus. **L'annexe 1 présente** un rappel sur les dictionnaires en langage Python.

1. 
- a. que renvoie l'instruction `flotte[26]` ?
- b. que renvoie l'instruction `flotte[80]["etat"]` ?
- c. que renvoie l'instruction `flotte[99]["etat"] ?`

2. Voici le script d'une fonction :
```python
def proposition(choix):
	for v in flotte:
		if flotte[v]["type"] == choix and flotte[v]["etat"] == 1:
			return flotte[v]["station"]
```

- a. **Quelles sont** les valeurs possibles de la variable `choix` ?
- b. **Expliquer** ce que renvoie la fonction lorsque l'on choisit comme paramètre l'une des valeurs possibles de la variable `choix`.

3. 
- a. Écrire un script en langage Python qui affiche les identifiants (`id_velo`) de tous les vélos disponibles à la station "Les Eucalyptus".
- b. Écrire un script en langage Python qui permet d'afficher l'identifiant (`id_velo`) et la station de tous les vélos électriques qui ne sont pas en panne.

4. On dispose d'une table de données des positions GPS de toutes les stations, dont un extrait est donné ci-dessous. Cette table est stockée sour forme d'un dictionnaire.  
   Chaque élément du dictionnaire est du type :  
		   'nom de la station' : (latitude, longitude)

```txt
stations = {
	'Jean Médecin' : (43.7017016, 7.2673351),
	'Les Eucalytpus' : (43.6756068, 7.2206844),
	'Ferber' : (43.6769012, 7.2283563),
	'CADAM' : (43.6767791, 7.1991651),
	
	}
```

On **admet** que l'on dispose d'une fonction `distance(p1, p2)` permettant de renvoyer la distance en mètres entre deux positions données par leurs coordonnées GPS (latitude et longitude).  
Cette fonction prend en paramètre deux tuples représentant les coordonnées des deux positions GPS et renvoie un nombre entier représentant cette distance en mètres.

Par exemple, `distance((49.8905, 2.2967), (49.8912, 2.3016))` renvoie 9591

**Écrire** une fonction qui prend en paramètre les coordonnées GPS de l'utilisateur sous forme d’un tuple et qui renvoie, pour chaque station située à moins de 800 mètres de l'utilisateur :
- le nom de la station ;
- la distance entre l'utilisateur et la station ;
- les identifiants des vélos disponibles dans cette station.

Une station où aucun vélo n’est disponible ne doit pas être affichée.

___
## Exercice 2 (BAC 0)
*Cet exercice porte sur la programmation en général et la récursivité en particulier.*

On considère un tableau de nombres de n lignes et p colonnes.  
Les lignes sont numérotées de 0 à n − 1 et les colonnes sont numérotées de 0 à p − 1. La case en haut à gauche est repérée par (0, 0) et la case en bas à droite par (n − 1, p − 1).  
On appelle chemin une succession de cases allant de la case (0, 0) à la case (n − 1, p − 1), en n’autorisant que des déplacements case par case : soit vers la droite, soit vers le bas.  
On appelle somme d’un chemin la somme des entiers situés sur ce chemin.  
Par exemple, pour le tableau T suivant :

|   |   |   |   |
| - | - | - | - |
| **4** | **1** | **1** | 3 |
| 2 | 0 | **2** | 1 |
| 3 | 1 | **5** | **1** |

- Un chemin est (0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3) (en gras sur le tableau);
- La somme du chemin précédent est 14.
- (0, 0), (0, 2), (2, 2), (2, 3) n’est pas un chemin.

L’objectif de cet exercice est de déterminer la somme maximale pour tous les chemins possibles allant de la case (0, 0) à la case (*n* − 1, *p* − 1).

**Question 1** On considère tous les chemins allant de la case (0, 0) à la case (2, 3) du tableau T donné en exemple.
1. Un tel chemin comprend nécessairement 3 déplacements vers la droite. Combien de déplacements vers le bas comprend-il ?
2. La longueur d’un chemin est égal au nombre de cases de ce chemin. Justifier que tous les chemins allant de (0, 0) à (2, 3) ont une longueur égale à 5.  
  
**Question 2** En listant tous les chemins possibles allant de (0, 0) à (2, 3) du tableau T, déterminer un chemin qui permet d’obtenir la somme maximale et la valeur de cette somme.  
  
**Question 3** On veut créer le tableau T’ où chaque élément T’\[i]\[j] est la somme maximale pour tous les chemins possibles allant de (0, 0) à (*i*, *j*).
1. Compléter et recopier sur votre copie le tableau T' donné ci dessous associé au tableau T :

|   |   |   |   |
| - | - | - | - |
| 4 | 1 | 1 | 3 |
| 2 | 0 | 2 | 1 |
| 3 | 1 | 5 | 1 |
T' = 

|   |   |   |   |
|:-:|:-:|:-:|:-:|
| 4 | 5 | 6 | ? |
| 6 | ? | 8 | 10 |
| 9 | 10 | ? | 16 |

**Question 4** Justifier que si *i* et *j* sont différents de 0, alors : T'\[i]\[j] = T\[i]\[j] + max(T'\[i-1]\[j], T'\[i]\[j-1]).

**Question 5** On veut créer la fonction récursive `somme_max` ayant pour paramètres un tableau T, un entier *i* et un entier *j*. Cette fonction renvoie la somme maximale pour tous les chemins possibles allant de la case (0, 0) à la case (i, j).  
1. Quel est le cas de base, à savoir le cas qui est traité directement dans faire appel à la fonction `somme_max` . Que renvoie-t-on dans ce cas ?
2. À l'aide de la question précédente, écrire en Python la fonction récursive `somme_max`.
3. Quel appel de fonction doit-on faire pour résoudre le problème initial ?


## Exercice 3 (BAC 2022 Mayotte-Liban)
*Cet exercice porte sur les structures de données (programmation objet)*

Dans un jeu de plateforme, des bulles de couleurs et de diamètres différents se déplacent de manière aléatoire. A chaque fois qu'une bulle touche une bulle plus grande, la petite cède son contenu à la plus grande, et donc celle-ci augmente de surface. Par exemple, si une bulle de 1 cm² rencontre une bulle de 4 cm², la petite bulle disparait et la plus grande a désormais une surface de 5 cm². A chaque collision, la vitesse de la grande bulle est réduite de moitié.
![Agar.io](https://agario-play.com/images/screenshots/60ab3120ad6d7.jpg)

Le développeur a choisi de coder en Python, chaque bulle est un objet disposant entre autre des attributs suivants :
- `xc`, `yc` sont deux entiers, les coordonnées du pixel placé au centre de la bulle,
- `rayon` est un entier, le rayon de la bulle en pixels,
- `couleur` est un entier, la couleur de la bulle
- `dirx`, `diry` sont deux décimaux (float) qui déterminent les déplacements à l'horizontale et à la verticale à chaque fois que la bulle se déplace. Ces deux valeurs déterminent donc la direction et la vitesse de la bulle. Par exemple si `dirx` vaut 0.5 et `diry` vaut 0.0, la bulle se déplace vers la droite uniquement alors que si `dirx` vaut -1.0 et `diry` vaut 0.0, la bulle se déplace vers la gauche et deux fois plus vite que précédemment.

On suppose que toutes les fonction de la bibliothèque `math` on déjà été importées par l'instruction `from math import *`.

La fonction `randint` de la bibliothèque `random` prend en paramètres deux entiers et renvoie un entier aléatoire dans la plage définie par les deux paramètres.  
Exemple : randint(-1, 5) peut renvoyer une des valeurs suivantes : -1, 0, 1, 2, 3, 4, 5.

1. Pour simplifier, on se limitera à un jeu de six bulles. Au départ on crée une liste appelée `Mousse` de longueur six contenant six emplacements vides :
	`Mousse = [None, None, None, None, None, None]`

Le code ci-dessous montre le début du programme et notamment la structure définition de la classe nommée `Cbulle` ainsi que le code permettant le déplacement d'une bulle.

```python
from random import randint
from math import *


class Cbulle:
	def __init__(self):
		self.xc = randint(0, 100)
		self.yc = randint(0, 100)
		self.rayon = randint(0, 10)
		self.dirx = float(randint(-1, 1)) # dirx et diry valent 
		self.diry = float(randint(-1, 1)) # -1.0 ou 0.0. ou 1.0 
		self.couleur = randint(1,65535)
	
	def bouge(self): # déplace la bulle 
		self.xc = self.xc + self.dirx
		self.yc = self.yc + self.diry
```
On crée les six bulles une à une et ces objets sont stockés dans les emplacements vides de la liste `Mousse`.  
`Mousse = [bulle1, bulle2, bulle3, bulle4, bulle5, bulle6]`  
Lors d’une collision, la bulle la plus petite disparait et est remplacée dans la liste par la valeur `None` tandis que la plus grosse a sa surface qui augmente.  
Au cours d’une partie, si une ou plusieurs bulles ont disparue, le programme peut en introduire de nouvelles dans le jeu : dans ce cas, lorsqu'une nouvelle bulle apparaît, elle remplace le premier `None` de la liste `Mousse`.

a) Recopier les quatre dernières lignes et compléter les `......` du code
	python ci-dessous.
```python
def donnePremierIndiceLibre(Mousse):
	"""
	  Mousse est une liste.
	  La fonction doit renvoyer l’indice du premier
	  emplacement libre (contenant None) dans la liste Mousse
	  ou renvoyer 6 en l’absence d’un emplacement libre dans
	  Mousse.
	"""
	i = 0
	while ………… and Mousse[i] != None :
		……………………
	return i
```

b) Lorsque le jeu crée une bulle (instance de la classe `Cbulle`), il doit ensuite
	la placer dans la liste `Mousse` à la place de `None`.  
	Écrire la fonction `PlaceBulle(b)` qui reçoit en paramètre un objet de type `Cbulle` et qui place cet objet dans la liste `Mousse`. Cette fonction ne renvoie rien, mais la liste `Mousse` est modifiée. Si aucun emplacement n'est disponible, la fonction ne modifie rien.

2. Pour le bon déroulement du jeu, on a besoin aussi d'une fonction `bullesEnContact(B1, B2)` qui renvoie `True` si la bulle `B2` touche la bulle `B1` et `False` dans le cas contraire.
	On peut remarquer que deux bulles sont en contact si la distance qui sépare leur centre est inférieur ou égale à la somme de leurs rayons.  
	On dispose de la fonction `distanceEntreBulles(B1, B2)` qui calcule et renvoie la distance entre les centres des bulles B1 et B2.
	Écrire la fonction `bullesEnContact(B1, B2)`.
![bulles rayon](https://raw.githubusercontent.com/TristanL06/private/main/image.png?token=GHSAT0AAAAAAB2MICB3GBVIW2VAFKOXZEGMY4EOTQQ)

3. Quand une petite bulle touche une plus grosse bulle, on appelle la fonction `collision`, ci-dessous, où `indPetite` est l'indice de la petite bulle et `indGrosse` l'indice de la grosse bulle dans `Mousse`.  
	Recopier et compléter les `.......` de la fonction `collision`

```python
def collision(indPetite, indGrosse, mousse):
	"""
	Absorption de la plus petite bulle d’indice indPetite
	par la plus grosse bulle d’indice indGrosse. Aucun test
	n’est réalisé sur les positions.
	"""
	# calcul du nouveau rayon de la grosse bulle
	surfPetite = pi*Mousse[indPetite].rayon**2
	surfGrosse = pi*Mousse[indGrosse].rayon**2
	surfGrosseApresCollision = ……………………………
	rayonGrosseApresCollision = sqrt(surfGrosseApresCollision/pi) 
	#réduction de 50% de la vitesse de la grosse bulle
	Mousse[indGrosse].dirx = …………………………
	Mousse[indGrosse].diry = …………………………
	#suppression de la petite bulle dans Mousse
	…………………………………………
```

___
## Annexe 1 (Exercice 1)

| Action | Instruction et syntaxe |
| :- | :- |
| Créer un dictionnaire vide | dico={} |
| Obtenir un élément d'un dictionnaire existant à partir de sa clé (*renvoie une erreur si cle n'existe pas dans le dictionnaire*)| dico\[cle] |
| Modifier la valeur d'un élément d'un dictionnaire à partir de sa clé |  dico\[cle]=nouvelle_valeur |
| ajouter un élément dans un dictionnaire existant | dico[nouvelle_cle]=valeur |
| Supprimer et obtenir un élément d'un dictionnaire à partir de sa clé | dico.pop(cle) |
| Tester l'appartenance d'un élément à un dictionnaire (renvoie un booléen) | cle in dico |
| Objet itérable contenant les clés. ce n'est pas un objet de type list | dico.keys() |
| Objet itérable contenant les valeurs. ce n'est pas un objet de type list | dico.values() |
| Objet itérable contenant les couples (clé,valeur) | dico.items() |
| Afficher les associations cle:valeur du dictionnaire dico | `for cle in dico:`    `print(cle, dico[cle])` |
