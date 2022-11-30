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
![croisement](https://github.com/TristanL06/Cyrano-NSI/raw/main/Chapitre%204%20:%20Piles%20et%20Files/Pasted%20image%2020221123221232.png)

- Écrire l'algorithme prenent en entrée les deux files et retournant la liste de sortie respectant les règles.

## Exercice 5 : Ascenceur

Un ascenseur fonctionne avec une structure de file.
Le principe de base est très simple : lorsqu'un utilisateur appuie sur le bouton d'appel de l'ascenceur l'appel est stocké dans la file d'attente de la mémoire de l'ascenceur.  
  
Pour implémenter cela en Python nous allons utiliser `print` et `input`. À chaque changement d'état de l'ascenceur on devra print les états de l'ascenceur et permettre à l'utilisateur d'entrer un nombre correspondant à l'étage qui appelle.  
On se limite ici aux étages de -2 à 15.  
Ajouter au fur et à mesure les fonctionnalités suivantes :
  
- Lorsqu'un appel est sur le trajet de l'ascenceur il passe prioritaire (dans le bon ordre des appels)
- Ajouter le fait que l'étage 0 est prioritaire sur tous les autres et doit être en tête de file dès qu'il est demandé
- Ajouter le sens de l'ascenceur, si on appel l'ascenceur à l'étage 8 pour aller à l'étage 9, il ne s'arrêtera pas s'il descend de l'étage 11 à l'étage 7 par exemple.

## Exercice 6 : Piles, Files et POO

Le langage Python ne possédant pas d'objet pouvant représenter une pile ou un file nous allons les créer :  
- Créer la classe `Pile` implémentant les méthodes :
	- estVide
	- empile
	- depile
	- sommet
	- taille
	- toString (renvoie un string de tous les éléments de la pile)

- Créer la classe `File` implémentant les méthodes :
	- estVide
	- enfile
	- defile
	- tete
	- taille
	- toString (renvoie un string de tous les éléments de la file)

- Ajouter à la classe Pile la méthode `toFile` qui retourne un objet File contenant toutes les données de la pile

- Ajouter à la classe File la méthode `toPile` qui retourne un objet Pile contenant toutes les données de la pile
