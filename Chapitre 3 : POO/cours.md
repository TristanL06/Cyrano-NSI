# Programmation Orientée Object (POO)

La **Programmation Orientée Object** permet de créer un outil qui aura des **attributs** (variables) et des **méthodes** (foctions).  
Ce **paradigme** a pour avantages de pouvoir regrouper dans une seule entité les données et fonctions utiles et de cacher les détails de l'exécution à l'utilisateur, ce qui permet l'**encapsulation**.

Comme la plupart des langages, Python utilise le concept de **classe**. Une classe est tout simplement une définition d'un object, un moule qui va permettre de construire les objets que l'on va utiliser.  
Pour écrire une Classe en Python il suffit d'utiliser le mot-clé `class` et de définir un `__init__` :
```python
class Cercle:
    def __init__(self, Cx, Cy, r):
        self.centre = (Cx, Cy)
        self.rayon = r
```
Ici on définit une classe Cercle qui définit un cercle dans le plan avec les coordonnées x et y de son centre, ainsi que son rayon. 
> Le premier paramètre de la méthode \_\_init\_\_ est nommé 'self' par convention, cela représente l'objet utilisé.

La syntaxe `self.rayon = r` permet de créer un nouvel attribut `rayon` pour l'object `self` et de lui donner pour valeur initiale la valeur du paramètre `r`.  
Voici l'utilisation que l'on peut faire de cet object actuellement :
```python
>>> c = Cercle(0,1,5)
>>> c.centre
(0,1)
>>> c.rayon
5
>>> c.rayon = 2
>>> c.rayon
2
```

On peut ajouter à notre classe Cercle un attribut `circonférence` :
```python
from math import pi

class Cercle:
    def __init__(self, Cx, Cy, r):
        self.centre = (Cx, Cy)
        self.rayon = r
        self.circonférence = 2*pi*r
```
Et demander la circonférence de l'object c1 créé :
```python
>>> c1 = Cercle(0,0,1)
>>> c1.circonférence
3.1514926
```

#### Les méthodes
Les **méthodes** sont des **fonctions internes** aux objects permettant d'exécuter du code uniquement lorsque c'est nécessaire, pour ne pas tout exécuter lors de la création de l'object (dans le `__init__`).  
Dans notre exemple du cercle on peut imaginer une méthode `distance` qui prend en argument un autre object *Cercle* et qui renvoie le flottant de la distance entre les centres des cercles :
```python
from math import pi

class Cercle:
    def __init__(self, Cx, Cy, r):
        self.centre = (Cx, Cy)
        self.rayon = r
        self.circonférence = 2*pi*r
        
	def distance(self, cercle2):
		x1, y1 = self.centre
		x2, y2 = cercle2.centre
		return ( (x1-x2)**2 + (y1-y2)**2 )**0.5
```

On peut maintenant ajouter la méthode `touche` qui renvoie un booléen (True si les deux cercles se touchent, False sinon) :
```python
class Cercle:
    def __init__(self, Cx, Cy, r):
        self.centre = (Cx, Cy)
        self.rayon = r
        self.circonférence = 2*pi*r
        
    def distance(self, cercle2):
        x1, y1 = self.centre
        x2, y2 = cercle2.centre
        return ( (x1-x2)**2 + (y1-y2)**2 )**0.5
		
    def touche(self, cercle2):
        distance = self.distance(cercle2)
        if distance < self.rayon + cercle2.rayon: #Si les deux cercles sont plus éloignés que la somme de leurs rayons ils ne se touchent pas
            if distance + min(self.rayon,cercle2.rayon) > max(self.rayon,cercle2.rayon): # Gère si on a un cercle contenu dans un autre
                return True
        return False 
```

On crée donc 3 cercles pour tester notre classe :
- Un cercle de centre (0,0) et de rayon 1
- Un cercle de centre (-2,1) et de rayon 1
- Un cercle de centre (2,3) et de rayon 3
- Un cercle de centre (2,3) et de rayon 2
```python
c1 = Cercle(0,0,1)
c2 = Cercle(-2,1,1)
c3 = Cercle(2,3,3)
c4 = Cercle(2,3,2)
```
*on a 4 **objects** créés à partir de la classe Cercle, qui ont chacun des attribus différents mais avec lesquels on peut intéragir de manière standardisée.*
![quatre cercles](https://raw.githubusercontent.com/TristanL06/Cyrano-NSI/main/Chapitre%203%20%3A%20POO/ressources/image.png)

Dans la console on peut donc exécuter :
```python
>>> c1.distance(c2)
2.23606797749979
>>> c3.distance(c4)
0.0
>>> c1.touche(c2)
False
>>> c1.touche(c3)
True
>>> c3.touche(c4)
False
```
