# TD de POO

## Exercice 1 : Géométrie dans le plan

#### Cet exercice traite de la modélisation en object de figures planes. Tous les éléments sont contenus dans l'espace plan déterminé par un repère cartésien (O,x,y).

1. Créer la Classe `Point`  qui prend en argument deux *int* et renvoie un objet ayant pour attribus `x` et `y`, les coordonnées du point
2. Créer la Classe `Segment` qui prend en paramètres deux *Point* et qui renvoie un objet ayant opur attribus `P1` et `P2`.
3. Ajouter à Segment l'attribut `longueur` calculé dans le `__init__` d'après la formule $L = \sqrt{(x_a - x_b)^2+(y_a - y_b)^2}$   
> On rappelle que $\sqrt{x} = x^{0,5}$  

4. Écrire la méthode `pente` dans la classe Segment qui renvoie le Flottant correspondant au coefficient directeur de la droite directrice du Segment.

Dans la suite de l'exercice on considère que la figure géométrique formée par les segments est fermée (chaque segment partage chacune de ses extrémités avec exactement un autre segment et aucun segment n'en coupe d'autre).

5. Créer la Classe `Figure` qui prend en paramètres une liste de segments et qui renvoie un objet ayant pour attribus `ListeSeg` la liste des segments et `nbAretes` le nombre d'arêtes'.
6. Écrire la méthode `Sommets` dans la classe `Figure` qui renvoie la liste des *Points* de la figure
7. Écrire la méthode `Périmètre` dans la classe `Figure` qui renvoie le périmètre de la figure sous forme de flottant.

On s'intéresse maintenant à l'aire de la figure

8. Écrire la méthode `estParallélogramme` qui renvoie *True* si la figure est un parallélogramme, *False* sinon.
9. Écrire la méthode `estTriangle` qui renvoie *True* si la figure est un triangle, *False* sinon.
10. Écrire la méthode `Aire` qui retour l'aire de la figure (Float) si c'est un triangle, `None` sinon
💡En informatique on peut calculer l'aire d'un triangle avec la formule de Héron : $S=\sqrt{p(p-a)(p-b)(p-c)}$ avec $p = \frac{a+b+c}{2}$ (a, b et c étant les longueurs des côtés du triangle)


## Exercice 2 : Compte en banque
*tiré du site [kxs](https://kxs.fr)*
Une banque souhaite mettre en place un système informatique basé sur la POO pour gérer les comptes de ses clients.

1. Créer une classe `Compte` modélisant un compte en banque. La classe possède trois attributs `idClient` `somme` et `taux` correspondant au numéro du client possédant le compte, à la somme placée sur le compte et au taux d'intérêt. Ces trois attributs doivent être affectés par le constructeur.
2. Ajoutez une méthode `affiche()` qui affiche la somme et le taux comme ci-dessous :  
   `Compte 17884	|	somme : 1000€	|	taux : 2%`  
   *La tabulation peut être écrite `\t` dans un print*
3. Ajouter la méthode `depot(x)` qui ajoute `x` à la somme sur le compte
4. Ajoutez la méthode `retrait(x)` qui enlève `x` à la somme sur le compte. Elle pourra renvoyer un erreur si la somme sur le compte devient négative et annuler alors l'opération.
5. Ajoutez la méthode `interets()` qui calcule les intérêts perçus en un an et les ajoute à la somme placée. Pour rappel les intérets se calculent avec la formule `interets = taux * somme / 100`

## Exercice 3 : Dates
*exercice tiré du site [NSI Waehren](https://nsiwaehren2.blogspot.com/)*
Dans cet exercice on va définir une classe `Date` pour représenter une date avec trois attributs `jour`, `mois` et `annee`, qui sont des entiers.
On se base sur le code suivant :
```python
class Date():
    def __init__(self,d,m,y):
        """ Création de la classe Date """
        if 1<=d<=31 and type(d)==int:   # vérification du numéro du jour : type et valeur
            self.jour=d
        else:
            raise ValueError("Numéro de jour impossible")
        if 1<=m<=12 and type(m)==int:  # vérification du numéro du mois : type et valeur
            self.mois=m
        else:
            raise ValueError("Numéro de mois impossible")
        self.annee=y
        self.noms=["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]  # noms des mois de l'année
        self.nbj=[31,28,31,30,31,30,31,31,30,31,30,31] # liste du nombre de jours par mois pour une année non bissextile
		
    def toString(self):
        """ Affichage d'une Date """
        pass
        
	    
    def bissextile(self):
        """ Test pour savoir si une Date correspond à une année bissextile """
        pass 
		
		
    def estAvant(self,d):
        """ Comparaison de deux Dates """
        pass
		
		
    def nombre_jours(self,d):
        """ Nombre de jours séparant deux Dates D et d """
        pass
```

1. Écrire la méthode `toString` qui renvoie une chaîne de caractère de la forme `"6 août 2001"`
2. Écrire la méthode `bissextile` qui renvoie `True` si la date est dans une année bissextile, False sinon.
3. Écrire la méthode `estAvant` qui renvoie `True` si la date définie par `self` est antérieure à la date `d`, False sinon
4. Écrire la méthode `nombre_jours` qui renvoie le nombre (int positif) de jours séparant deux dates.

	Question Bonus : L'API du gouvernement `https://data.education.gouv.fr/api/records/1.0/search/?dataset=fr-en-calendrier-scolaire&facet=description&facet=start_date&facet=end_date&refine.location=Nice` permet de récupérer les dates des vacances scolaires.
	Modifiez et utilisez la Classe Date pour obtenir le nombre de jours avant les prochaines vacances.

## Exercice supplémentaires (idées, difficile)

- Loup Garou :
		- Système de jeu avec cartes, extensions...

- Pokémon :
		- Système de jeu avec cartes, énergies, combat, équipe...

- Arborescence de fichiers :
		- Parcourir des fichiers de manière récursive et enregistrer le parent/ les enfants
		- système d'affichage de l'arborescence (commande `tree`)

- Agario :
		- Gérer les joueurs, la nourriture, les collisions, la taille, la vitesse...
