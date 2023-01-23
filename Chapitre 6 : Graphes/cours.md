# Chapitre 6 : Les graphes

Les graphes sont un autre outil de modélisation mathématique utilisé pour représenter des relations entre des objets. Ils ont de nombreuses applications, notamment en informatique, en réseaux, en transport et en sciences sociales.

[ ![GOT personnages](https://assets.datacamp.com/production/project_76/img/got_network.jpeg) ](https://www.kaggle.com/code/mmmarchetti/game-of-thrones-network-analysis)  *Ici on peut voir un graph représentant des relations entre des personnes.*

[![Twitch relations](https://pbs.twimg.com/media/E29MElYXEAMjCFa?format=jpg&name=large)](https://www.youtube.com/watch?v=N61_kHXpaFA)  instantané de Twitch [*zoomer dedans*](https://www.easyzoom.com/imageaccess/6ef899188b964819a95a286fcb422635)

Il y a deux grandes familles de graphes, les graphes **orientés** et les graphes **non orientés**. Ils ont chacun des fonctions et des utilités différentes. Ils ont même un vocabulaire spécifique à chacun.  
Pour expliquer rapidement la différence, dans un graphe orienté les liaison entre les sommets sont orientées dans une unique direction.

## ➖ Les graphes non orientés
Dans un graphe **non orienté** les **sommets** sont reliés par des **arêtes**. Si tous les sommets sont reliés entre eux le graphe est **connexe**. Une suite de sommets **adjacents** est une **chaîne** et une chaîne ayant pour point de départ et point d'arrivée le même sommet est un **cycle**.  

C'est plus simple de visualiser sur un exemple :  
![graphe non orienté wikipédia](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/220px-6n-graf.svg.png)  

Ici on a 1,2,3... qui sont des **sommets**. Ils sont reliés par des arêtes.  
Tous les sommets sont reliés donc le graphe est **connexe**.  
6-4-5-1-2 est une **chaîne** (une chaîne peut passer plusieurs fois par le même sommet).  
5-1-2-5 est un **cycle**.

## ➡ Les graphes orientés
Dans un graphe **orienté** les **sommets** sont reliés par des **arcs**. Si tous les sommets sont reliés entre eux le graphe est **connexe** et s'il est possible d'aller de n'importe quel sommet à n'import quel autre, il est **fortement connexe**. Une suite de sommets **adjacents** est un **chemin** et un chemin ayant pour point de départ et point d'arrivée le même sommet est un **cycle**.  

Par exemple :
![graphe orienté wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Directed_graph_no_background.svg/220px-Directed_graph_no_background.svg.png)  
Ici on a 1,2,3,4 qui sont les **sommets** du graphe. Ils sont reliés par des **arcs**.  
Tous les sommets sont reliés donc le graphe est **connexe**.  
Tous les sommets ne sont pas atteignables depuis n'importe que sommet (1 ne peut jamais être atteint), le graphe n'est pas **fortement connexe**.  
1-3-4 est un **chemin**.
3-4-3 est un **cycle**.


#### Il existe encore quelques définitions à connaître :
- Graphe complet : graphe dans lequel tous les sommets sont reliés entre eux. 
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8SgZSVzZNwD2N7-8_I4y4V7xG6ZOJ7I-LZw&usqp=CAU)
* Ordre d'un graphe : nombre de sommets du graphe.
* Degré d'un sommet : nombre d'arrêtes reliées à un sommet.
* Sommets adjacents : deux sommets reliés par un une arête ou un arc, quel que soit l'orientation de ce dernier


## Les graphes pondérés
Un graphe **pondéré** est un graphe dont chaque arête, ou chaque arc, a un **poids**.  
Ce type de graphe permet d'inclure des distances, des temps, des coûts dans les calculs de parcours du graphe.  


![graphe non pondéré](https://graphonline.ru/tmp/saved/lN/lNQLWfJKitBeXNHt.png)  
Dans cet exemple, pour aller du sommet 3 au sommet 2 on peut utiliser les chaînes 3-5-2 ou 3-4-2. Ce sont les plus logiques car elles nous paraissent les plus courtes.  
Maintenant si on rajoute comme poids des arêtes le temps de parcours :  
![Graphe pondéré](https://graphonline.ru/tmp/saved/eS/eSGGqrmTiXzloqaG.png)  
On remarque immédiatement que le trajet le plus rapide est de passer par le haut du graphe avec la chaîne 3-1-0-2, qui a un poids de 3.  
Les chaînes précédentes ont maintenant un poids total de 11 et 12 respectivement.


## Les représentations des graphes

### Représentation matricielle
On peut représenter un graphe par une matrice d'adjacence. La matrice d'adjacence permet de stocker toutes les informations, des orientations ainsi que des poids.  
La matrice d'adjacence du graphe  
![graphe matriciel](https://graphonline.ru/tmp/saved/Ke/KewGgpQBxlUAOwCS.png)  
est représentable par la matrice d'adjacence associée 
```txt
0, 1, 2, 
4, 0, 1, 
8, 0, 0, 
```
La case (`i;j`) (`i`ème ligne et `j`ème colonne) sera égale au nombre d’arêtes reliant la lettre de la `i`ème à la lettre de la `j`ème colonne.  
Dans un graphe non orienté, comme il n’y a pas de sens, la matrice sera toujours symétrique !

Calculs avec les matrices associées : 
Soit M la matrice non pondérée associée à un graphe, la matrice M<sup>x</sup> donne le nombre de chemins allant de `i` à `j` en `x` étapes exactement.

## Algorithmes sur les graphes

### Distance entre deux sommets :
- longueur de la plus courte chaîne qui les relie.

### Diamètre :
- Longueur de la plus grande chaîne

Il y a plusieurs algorithmes couramment utilisés pour travailler avec les graphes, notamment :

### L'algorithme de Dijkstra :
L’algorithme de Dijkstra permettant de déterminer le plus court chemin entre deux points dans un graphe.

Pour regarder comment il fonctionne on va reprendre le graphe pondéré ci-dessus :  
![Graphe pondéré](https://graphonline.ru/tmp/saved/eS/eSGGqrmTiXzloqaG.png)  

On commence par tracer un tableau dont chaque colonne représente un sommet : 
| 0 | 1 | 2 | 3 | 4 | 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|
|   |   |   |   |   |   |


On choisit ensuite notre sommet de départ (ici on prend 0 par exemple). On met alors 0 dans la colonne du sommet de départ et on tire un trait.
| 0 | 1 | 2 | 3 | 4 | 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 |   |   |   |   |   |
| \| |   |   |   |   |   |

On ajoute ensuite dans les colonnes de tous les sommets adjacents la distance pour y parvenir et la distance parcourue :  
| 0 | 1 | 2 | 3 | 4 | 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 - 0 | 1 - 0 |   |   |   |
| \| |   |   |   |   |   |

On s'occupe maintenant du sommet de poids le plus faible (en cas d'égalité on choisit celui que l'on veut, ici le 1). On tire un trait dans la colonne et on remplit les colonnes des adjacents :  
| 0 | 1 | 2 | 3 | 4 | 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 - 0 | 1 - 0 |   |   |   |
| \| | \| |   | 2 - 1 |   |   |

Et on répète cette étape jusqu'à avoir barré toutes les colonnes sauf une

| 0  | 1     | 2     | 3     | 4     | 5     |
|:---:|:-----:|:-----:|:-----:|:-----:|:-----:|
| 0  | 1 - 0 | 1 - 0 |       |       |       |
| \| | \|    |       | 2 - 1 |       |       |
| \| | \|    | \|    |       | 7 - 2 | 8 - 2 |

En partant de 3, les sommets adjacents sont 5 et 4, à une distance de 4 et 6, que l'on ajoute donc à 2 et on garde le minimum de chaque :  
| 0  | 1     | 2     | 3     | 4     | 5     |
|:---:|:-----:|:-----:|:-----:|:-----:|:-----:|
| 0  | 1 - 0 | 1 - 0 |       |       |       |
| \| | \|    |       | 2 - 1 |       |       |
| \| | \|    | \|    |       | 6 - 2 | 8 - 2 |
| \| | \|    | \|    |   \|    |  | 7 - 3 |

Les sommets adjacents à 4 sont déjà complets, on trace donc le trait dans la colonne 4 :  
| 0  | 1     | 2     | 3     | 4     | 5     |
|:---:|:-----:|:-----:|:-----:|:-----:|:-----:|
| 0  | 1 - 0 | 1 - 0 |       |       |       |
| \| | \|    |       | 2 - 1 |       |       |
| \| | \|    | \|    |       | 6 - 2 | 8 - 2 |
| \| | \|    | \|    |   \|    |  | 7 - 3 |
| \| | \|    | \|    |   \|    | \| |  |

Et enfin le dernier sommet n'a aucun adjacent non complet, on trace un trait dans la colonne 5 et on a terminé :  
| 0  | 1     | 2     | 3     | 4     | 5     |
|:---:|:-----:|:-----:|:-----:|:-----:|:-----:|
| 0  | 1 - 0 | 1 - 0 |       |       |       |
| \| | \|    |       | 2 - 1 |       |       |
| \| | \|    | \|    |       | 6 - 2 | 8 - 2 |
| \| | \|    | \|    |   \|    |  | 7 - 3 |
| \| | \|    | \|    |   \|    | \| |  |
| \| | \|    | \|    |   \|    | \| | \| |

> Pour lire ce tableau il faut regarder la dernière ligne contenant des chiffres de chaque colonne. Par exemple ici `2 - 1` signifie que le plus court chemin pour atteindre le sommet 3 a un coût de 2 et passe par le sommet 1.  
> Si on regarde le sommet 1, `1 - 0` signifie que l'atteindre a un coût de 1 en passant par 0.  
> En remontant donc la chaîne, le chemin le plus court entre 0 et 3 est la chaîne `0 - 1 - 3`.

Cet algorithme donne les meilleurs chemins pour aller de l'origine à tous les sommets du graphe, il est cependant assez coûteux en ressources car il test de très nombreuses possibilités et devient lent quand le graphe devient grand. Pour le fonctionnement réel des GPS il lui est préféré des algorithmes plus efficaces (A*) qui ne donnent cependant pas toujours le meilleur trajet.


Il existe également les algorithmes suivants, qui sont plus compliqués et totalement hors-programme :
- Algorithme de Bellman-Ford pour détecter les cycles négatifs
- Algorithme de Kruskal pour trouver l'arbre couvrant de poids minimum
- Algorithme de Prim pour trouver l'arbre couvrant de poids minimum
- Algorithme de Floyd-Warshall pour résoudre le **problème du plus court chemin** entre tous les sommets.

Il est important de noter que les graphes peuvent être très complexes et qu'il peut y avoir plusieurs approches pour résoudre un même problème sur les graphes. Il est donc important de bien comprendre les concepts fondamentaux et les algorithmes pour pouvoir utiliser les graphes efficacement dans les différents domaines d'application.

___
Ressources :

tableau du vocabulaire :
| Graphes non orientés | Graphes Orientés |
| :-: | :-: |
| arêtes | arcs |
| chaîne | chemin |
| connexe | connexe |
| ... | fortement connexe |
| --- | --- |
| Liste des voisins | Liste des successeurs |

Définitions supplémentaires :

- Chaîne **élémentaire** : chaine dans laquelle aucun sommet n’apparaît plus d’une fois.
- Chaîne **simple** : chaîne dans laquelle aucune arête n'apparaît plus d'une fois
- Boucle : arête d'un sommet à lui-même
- Graphe **simple** : absence de boucle et au plus une arête entre deux sommets
- Multigraphe : Graphe non simple
- Chaîne **Eulérienne** : chaîne contenant une et une seule fois toutes les arêtes du graphe (les sommets peuvent apparaitre plusieurs fois).
	> Un graphe possède une chaîne eulérienne si et seulement si le nombre de sommets de degré impair est 0 ou 2
- Nombre chromatique : nombre minimales de couleurs pour colorier chaque sommet sans que deux sommets adjacents aient la même couleur
	> Si le plus haut degré des sommets est noté x, alors le nombre chromatique est au plus égal à x + 1.

## Particularités eulériennes :

Une chaîne **eulérienne** est une chaîne contenant une et une seule fois toutes les arêtes du graphe (les sommets peuvent apparaitre plusieurs fois).  
Un graphe possède une chaîne eulérienne si et seulement si le nombre de sommets de degré impair est 0 ou 2.  
Si c'est 0 la chaîne Eulérienne peut être démarrée par n'importe quel sommet.  
Si c'est 2 la chaîne Eulérienne commence à l'un des sommets de degré impaire et termine par l'autre.  

Un **cycle eulérien** est un cycle contenant une et une seule fois toutes les arêtes du graphe, il s'agit donc d'un chaîne eulérienne revenant à son point de départ.
Un graphe possède un cycle eulérien si et seulement si tous les sommets sont de degré pair.

## Particularités hamiltoniennes :

Les chaînes et cycles hamiltoniens sont analogues aux chaînes et cycles eulériens, mais concernent les sommets.

Une **chaîne** est **hamiltonienne** si elle passe une et une seule fois par tous les sommets du graphe.  

Un **cycle** est **hamiltonien** s’il passe une et une seule fois par tous les sommets du graphe (le sommet de départ et d'arrivée et compté comme un unique sommet).
