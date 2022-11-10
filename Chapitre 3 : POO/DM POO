# DM de NSI n°1 : POO
### À rendre pour le 17/11/2022

#### Ce DM traite de la modélisation en object de figures planes. Tous les éléments sont contenus dans l'espace plan déterminé par un repère cartésien (O,x,y).

1. Créer la Classe `Point`  qui prend en argument deux *int* et renvoie un objet ayant pour attribus `x` et `y`, les coordonnées du point.
2. Créer la Classe `Segment` qui prend en paramètres deux *Point* et qui renvoie un objet ayant opur attribus `P1` et `P2`.
3. Ajouter à Segment l'attribut `longueur` calculé dans le `__init__` d'après la formule $L = \sqrt{(x_a - x_b)^2+(y_a - y_b)^2}$.  
> On rappelle que $\sqrt{x} = x^{0,5}$.  

4. Écrire la méthode `pente` dans la classe Segment qui renvoie le Flottant correspondant au coefficient directeur de la droite directrice du Segment.

Dans la suite de l'exercice on considère que la figure géométrique formée par les segments est fermée (chaque segment partage chacune de ses extrémités avec exactement un autre segment et aucun segment n'en coupe d'autre).

5. Créer la Classe `Figure` qui prend en paramètres une liste de segments et qui renvoie un objet ayant pour attribus `ListeSeg` la liste des segments et `nbAretes` le nombre d'arêtes'.
6. Écrire la méthode `Sommets` dans la classe `Figure` qui renvoie la liste des *Points* de la figure
7. Écrire la méthode `Périmètre` dans la classe `Figure` qui renvoie le périmètre de la figure sous forme de flottant.

On s'intéresse maintenant à l'aire de la figure.

8. Écrire la méthode `estParallélogramme` qui renvoie *True* si la figure est un parallélogramme, *False* sinon.
9. Écrire la méthode `estTriangle` qui renvoie *True* si la figure est un triangle, *False* sinon.
10. Écrire la méthode `Aire` qui retour l'aire de la figure (Float) si c'est un triangle, `None` sinon.  
💡En informatique on peut calculer l'aire d'un triangle avec la formule de Héron : $S=\sqrt{p(p-a)(p-b)(p-c)}$ avec $p = \frac{a+b+c}{2}$ (a, b et c étant les longueurs des côtés du triangle).
