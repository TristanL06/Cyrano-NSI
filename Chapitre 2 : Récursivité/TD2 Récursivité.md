## TD guidé

#### Exercice 1 : Dichotomie
> Pour tout cet exercice on considère que la liste fournie en entrée est triée, il n'est donc pas nécessaire de le vérifier.
1. Écrire une fonction `dichotomie(liste, x)` prenant en entrée une liste triée et retournant `True` si  la liste contient l'élément `x`, `False` sinon.
2. Écrire une fonction récursive ``dichotomieR(liste, x)`` qui a la même utilité qu'à la question 1 en utilisant le principe de "diviser pour régner".
3. L'utilisaton de la fonction `len()` et le *slicing* sont assez couteux algorithmiquement, imaginer donc une fonction récursive ``dichotomieR(liste, x, i, j)`` à partir de la réponse précendente qui n'utilise pas ces deux éléments.
___
#### Exercice 2 : Suite de Fibonacci
La suite de Fibonacci est déterminée mathématiquement par :
$$\begin{cases}
U_0 = 0 \\
U_1 = 1 \\
U_{n+2} = U_{n} + U_{n+1}
\end{cases}$$
Écrire la fonction récursive `fibo(n)` qui prend en entrée un entier n strictement supérieur à 0 et renvoie la n-ième valeur de la suite de fibonacci (ex : fibo(7) = 13)

> :warning: En raison de la complexité ne pas dépasser fibo(35)

___
#### Exercice 3 : Tri Fusion

Le tri fusion fonctionne en utilisant le *slicing* (en coupant une liste en deux) jusqu'à n'avoir plus qu'un seul élément avant de recombiner les éléments dans le bon ordre.

![Tri Fusion](https://upload.wikimedia.org/wikipedia/commons/6/60/Mergesort_algorithm_diagram.png)

C'est une méthode de tri récursif.

Écrivez la fonction récursive du tri fusion.
___
#### Exercice 4 : Un peu de pratique
Pour chacune des expressions mathématiques suivantes, écrire une fonction classique qui résout le problème, puis une fonction récursive qui le fait également.
1. $a + b$ : `somme(a, b)`
2. a ! : `factorielle(a)`
3. $a^b$ : `puissance(a, b)`
___
#### Exercice 5 : Tour de Hanoï
> :brain: Pour faire fumer un peu le cerveau, et surtout pour la culture générale
> Source : [Wikipédia]([Tours de Hanoï — Wikipédia (wikipedia.org)](https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF))

![tours de Hanoï](https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Tower_of_Hanoi.jpeg/260px-Tower_of_Hanoi.jpeg)
Les tours de Hanoï (originellement, **la tour d'Hanoï**) sont un jeu de réflexion imaginé par le mathématicien français Édouard Lucas, et consistant à déplacer des disques de diamètres différents d'une tour de « départ » à une tour d'« arrivée » en passant par une tour « intermédiaire », et ceci en un minimum de coups, tout en respectant les règles suivantes :
- on ne peut déplacer plus d'un disque à la fois ;
- on ne peut placer un disque que sur un autre disque plus grand que lui ou sur un emplacement vide.

On suppose que cette dernière règle est également respectée dans la configuration de départ.

**Exercice :** Écrire une fonction récursive permettant de résoudre le problème des tours de Hanoï à **N** disques

> Énoncé original des tours de Hanoï :
> *N. Claus de Siam a vu, dans ses voyages pour la publication des écrits de l'illustre Fer-Fer-Tam-Tam, dans le grand temple de Bénarès, au-dessous du dôme qui marque le centre du monde, trois aiguilles de diamant, plantées dans une dalle d'airain, hautes d'une coudée et grosses comme le corps d'une abeille. Sur une de ces aiguilles, Dieu enfila au commencement des siècles, 64 disques d'or pur, le plus large reposant sur l'airain, et les autres, de plus en plus étroits, superposés jusqu'au sommet. C'est la tour sacrée du Brahmâ. Nuit et jour, les prêtres se succèdent sur les marches de l'autel, occupés à transporter la tour de la première aiguille sur la troisième, sans s'écarter des règles fixes que nous venons d'indiquer, et qui ont été imposées par Brahmâ. Quand tout sera fini, la tour et les brahmes tomberont, et ce sera la fin des mondes !*


## Recherche récursive dans un répertoire

La récursivité est très utilisée pour fouiller dans des dossiers. Pour cela on peut utiliser la bibliothèque `os` en python. On commence donc par l'importer avec la ligne `import os`.

Voici quelques fonctions utiles :
```txt
abspath(path)             →   Retourne un chemin absolu
dirname(p)                →   Retourne le dossier parent de l'élément
exists(path)              →   Test si un chemin existe
getaTime(filename)        →   Retourne la date du dernier accès au fichier
getmTime(filename)        →   Retourne la date de la dernière modification du fichier
isdir(s)                  →   Test si le chemin est un dossier
isfile(path)              →   Test si le chemin est un fichier
```

Créez un "virus" qui parcourera tous les fichiers d'un répertoire et créer des stats, par exemple :
- Pourcentage de fichiers texte
- taille totale de tous les fichiers
- nombre de fichiers et dictionnaires
- arborescence (tree)
