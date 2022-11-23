# TD Piles et Files

Pour tout le TD les piles et les files ne doivent pas être modifiées lors de l'exécution, sauf si c'est expressément demandé.

## Exercice 1 : Implémenter les Piles avec des fonctions

1. Écrire la fonction `estVide` qui prend en argument une Pile et renvoie `True` si elle est vide, `False` sinon
2. Écrire la fonction `sommet` qui prend en argument une Pile et renvoie la valeur du premier élément de la pile (`None` si la pile est vide)
3. Écrire la fonction `depile` qui prend en argument une Pile, enlève le premier élément et le renvoie, `None` si vide.
4. Écrire la fonction `empile` qui prend en argument une Pile et un élément et ajoute l'élément au sommet de la pile.

## Exercice 2 : Implémenter les Files avec des fonctions

1. Écrire la fonction `estVide` qui prend en argument une File et renvoie `True` si elle est vide, `False` sinon
2. Écrire la fonction `tete` qui prend en argument une File et renvoie la valeur du premier élément de la file (`None` si la file est vide)
3. Écrire la fonction `avance` qui prend en argument une File, enlève le premier élément et le renvoie, `None` si vide.
4. Écrire la fonction `enfile` qui prend en argument une File et un élément et ajoute l'élément à la queue de la file.

## Exercice 3 : Définition plus avancée des Piles/Files
*dans cet exercice les fonctions définies précedemment devront être utilisées*

1. Écrire la fonction `taillePile` prenant en argument une Pile et renvoyant la taille de la Pile
2. Écrire la fonction `pileInclus` prenant en argument une Pile et un élément, et renvoyant `True` si l'élément est dans la Pile, `False` sinon.
3. Écrire la fonction `maxPile` prenant en argument une Pile et renvoyant l'élement maximal de la pile.
4. Écrire la fonction `affichePile` prenant en argument une Pile et affichant les éléments de la pile ligne par ligne.
 
5. Faire les 4 questions précédentes avec les Files.

## Exercice 4 : Enfin du concret, croisement routier

On a deux files représentant deux routes se rencontrant à un croisement. La route 2 a un *céder-le-passage* donc si dex voitures arrivent en même temps en bout de file c'est la voiture 1 qui passe.
La file 3 représente la route 3, route de sortie :  
![croisement]("Pasted image 20221123221232.png")

- Écrire l'algorithme prenent en entrée les deux files et retournant la liste de sortie respectant les règles.

