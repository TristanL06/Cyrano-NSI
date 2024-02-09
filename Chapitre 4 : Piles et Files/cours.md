# Les Piles et les Files

Les **piles** et les **files** sont des types n'existant pas formellement en Python. Pour les exploiter nous utiliserons donc dans un premier temps les **listes** en se restreignant à quelques commandes basiques.

## Les PILES 
Les piles sont des objets FILO (First In Last Out), c'est-à-dire que les valeurs entrées en premier ne peuvent être récupérées que en dernier. Exactement comme une pile de crêpes, la première crêpe cuite sera mangée en dernier.  
La représentation la plus courante est celle d'une pile de dossiers. Pour accéder à celui qui est en dessous on doit enlever ceux d'au dessus un par un.  
![pile](https://pixy.org/src/452/thumbs350/4522322.jpg)

Concernant les Piles on peut donc définir quatre opérations :
- Regarder si la pile est vide
- Regarder l'élément au sommet de la pile
- Enlever l'élément au sommet de la pile
- Ajouter un élément sur la pile

Imaginon que l'on a la pile suivante :  
```txt
┌───┐  
│ 5 │  
├───┤  
│ 4 │  
├───┤  
│ 8 │  
├───┤  
│ 6 |  
├───┤  
│ 3 │  
├───┤  
│ 2 │  
└───┘  
```
  
Voici successivement un dépilement, puis un empilement de la valeur 8
```txt
 - depile -> 
╔═══╗      ╔═══╗       ╔═══╗
║ 5 ║      ║   ║       ║ 8 ║
╠═══╣      ╠═══╣       ╠═══╣
║ 4 ║      ║ 4 ║       ║ 4 ║
╠═══╣      ╠═══╣       ╠═══╣
║ 8 ║      ║ 8 ║       ║ 8 ║
╠═══╣      ╠═══╣       ╠═══╣
║ 6 ║      ║ 6 ║       ║ 6 ║
╠═══╣      ╠═══╣       ╠═══╣
║ 3 ║      ║ 3 ║       ║ 3 ║
╠═══╣      ╠═══╣       ╠═══╣
║ 2 ║      ║ 2 ║       ║ 2 ║
╚═══╝      ╚═══╝       ╚═══╝
             - empile(8) ->
```

Pour travailler sur les piles en Python on se limitera aux fonctions :
| opération | Fonction en Python |
| - | - |
| regarder si la pile est vide | `not not Pile` |
| regarder le sommet de la pile | `Pile[-1]` |
| Enlever l'élément au sommet | `Pile.pop()` |
| Ajouter un élément à la pile | `Pile.append(element)` |


## Les files

Les files sont des objets FIFO (First In First Out), c'est-à-dire que les valeurs entrées en premier sont récupérées en premier. Exactement comme dans une file d'attente, le premier arrivé sera le premier servi.  
![file](https://thumbs.dreamstime.com/b/les-gens-dans-la-file-d-attente-15346257.jpg)

Pour les files, les opérations autorisées sont quasiment les mêmes que pour les piles :
- Regarder le premier élément de la file
- Ajouter un élément à la file
- Enlever le premier élément de la file
- Regarder si la file est vide

Pour travailler sur les files en Python on se limitera aux fonctions :
| opération | Fonction en Python |
| - | - |
| regarder si la file est vide | `not File` |
| regarder début de la file | `File[0]` |
| Enlever le premier élément | `File.pop(0)` |
| Ajouter un élément à la file | `File.append(element)` |

# Voir TD pour plus de détails
