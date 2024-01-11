# Chapitre 5
## Introduction à l'agorithmique

## 1. Principe
Un algorithme est une suite d'instructions permettant de résoudre un problème. Il est composé de trois parties :
- **Entrée** : les données nécessaires à la résolution du problème
- **Traitement** : les instructions permettant de résoudre le problème
- **Sortie** : les résultats de l'algorithme

Un des grands intérêt de l'informatique est de pouvoir automatiser des tâches répétitives. Pour cela, il faut pouvoir répéter un traitement un certain nombre de fois. On utilise pour cela des **boucles**. Le piège est de ne pas voir que l'on répète un grand nombre de fois une opération qui pourraît être simplifiée. Il faut donc trouver un moyen de simplifier le traitement.  
Mesurer cette optimisation est un des objectifs de l'algorithmique. On utilise pour cela la notion de **complexité**.  
Il existe deux types de complexité :
- **La complexité en temps** : le temps nécessaire à l'exécution de l'algorithme
- **La complexité en espace** : la mémoire nécessaire à l'exécution de l'algorithme

Nous allons ici uniquement nous intéresser à la complexité en temps.  
Pour aprofonfir le sujet, vous pouvez consulter le livre de [Sylvain Perifel
 **COMPLEXITÉ ALGORITHMIQUE**](https://www.irif.fr/~sperifel/complexite.pdf).

## 2. Complexité en temps
La complexité en temps est le nombre d'opérations élémentaires nécessaires à l'exécution de l'algorithme. En effet, le temps d'exécution d'un algorithme dépend de la puissance de l'ordinateur sur lequel il est exécuté. Celui-ci ne pouvant être connu à l'avance (on ne sait pas sur quel ordinateur l'algorithme sera exécuté), on ne peut pas utiliser ce critère pour mesurer la complexité d'un algorithme.  
On utilise alors le nombre d'opérations élémentaires nécessaires à l'exécution de l'algorithme. Ce nombre est représenté sous la forme $O(n)$ (prononcer "Grand O de n") où $n$ est la taille de l'entrée.

### Exemple 1
La fonction `max(L)` qui renvoie le plus grand élément d'une liste `L` :
```python
def max(L):
    m = L[0]
    for i in range(1, len(L)):
        if L[i] > m:
            m = L[i]
    return m
```
On peut voir que on fait un tour de boucle pour chaque élément de la liste `L`. On dit que la complexité de cette fonction est $O(n)$ avec $n$ la taille de la liste `L`.

### Exemple 2
L'algorithme de tri par insertion a une complexité $O(n^2)$ avec $n$ la taille de la liste à trier. On a ajouté une fonction `verif_tri(L)` qui permet de vérifier que la liste `L` est triée avant de faire les opérations.
```python
def tri_insertion(L):
    if verif_tri(L):
        return
    for i in range(1, len(L)):
        x = L[i]
        j = i
        while j > 0 and L[j - 1] > x:
            L[j] = L[j - 1]
            j = j - 1
        L[j] = x

def verif_tri(L):
    for i in range(1, len(L)):
        if L[i] < L[i - 1]:
            return False
    return True
```
la fonction `verif_tri(L)` permet de vérifier que la liste `L` est bien triée, elle a une complexité $O(n)$. Si on l'utilise pour vérifier que la liste `L` est bien triée après l'avoir triée avec la fonction `tri_insertion(L)`, on a une complexité $O(n^2) + O(n) = O(n^2)$.



### Notions importantes
- On ne s'intéresse qu'aux ordres de grandeur. On ne s'intéresse pas aux constantes. Si on a une complexité $O(2n)$, on dira que la complexité est $O(n)$. Pour reprenre l'exemple 1, on a `m = L[0]` au début et deux opérations à chaque tour de boucle. On a donc $2n + 1$ opérations. On dira quand-même que la complexité est $O(n)$ car ce qui nous intéresse est l'ordre de grandeur.  
- On ne s'intéresse qu'au pire des cas. Pour reprendre l'exemple 2, on a une complexité $O(n^2)$ car c'est le pire des cas. En effet, si la liste est déjà triée, on n'entre pas dans la boucle `while` et on a une complexité réelle en $O(n)$.


## 3. Cas concrets

### fibonacci
La suite de Fibonacci est une suite d'entiers dans laquelle chaque terme est la somme des deux termes qui le précèdent. Elle commence généralement par les termes 0 et 1 (parfois 1 et 1) et ses premiers termes sont :
```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```
On peut définir la suite de Fibonacci par la relation de récurrence suivante :
$$
\left\{
    \begin{array}{ll}
        u_0 = 0 \\
        u_1 = 1 \\
        u_n = u_{n-1} + u_{n-2}
    \end{array}
\right.
$$

On peut définir une fonction `fibonacci(n)` qui renvoie le $n$-ième terme de la suite de Fibonacci :
```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```
On peut voir que la fonction `fibonacci(n)` est définie par récurrence. On a donc une complexité $O(2^n)$. Les appels récursifs du fibo(4) sont représentés par un arbre de récursion :
![Alt text](arbre_binaire.png)

Et là on remarque immédiatement que l'on fait beaucoup de calculs en double, en triple voire pire. On peut donc optimiser la fonction `fibonacci(n)` en utilisant un dictionnaire pour stocker les résultats déjà calculés :
```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in dico:
        return dico[n]
    dico[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dico[n]
```
On a donc une complexité $O(n)$.

### tri fusion

Le tri fusion est un algorithme de tri qui utilise la technique de diviser pour régner. Il est basé sur la récursivité.
On divise la liste en deux parties égales. On trie chacune des deux parties. On fusionne les deux parties triées. 
    
```python
def tri_fusion(L):
    if len(L) <= 1:
        return L
    L1 = tri_fusion(L[:len(L)//2])
    L2 = tri_fusion(L[len(L)//2:])
    return fusion(L1, L2)

def fusion(L1, L2):
    L = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L.append(L1[i])
            i = i + 1
        else:
            L.append(L2[j])
            j = j + 1
    if i < len(L1):
        L.extend(L1[i:])
    if j < len(L2):
        L.extend(L2[j:])
    return L
```

On peut voir que la fonction `tri_fusion(L)` est définie par récurrence, avec une complexité $O(n\log(n))$.

Les algorithmes de tri sont très importants en informatique, et un jeu très prisé pour tous les mathématiciens et algorithmiciens. Il existe de nombreux algorithmes de tri. Vous pouvez consulter [cette page](https://fr.wikipedia.org/wiki/Algorithme_de_tri) pour en savoir plus.

### recherche dichotomique
La recherche dichotomique est un algorithme de recherche d'un élément dans un tableau trié. Il est basé sur la technique de diviser pour régner. On divise le tableau en deux parties égales. On compare l'élément recherché avec l'élément au milieu du tableau. Si l'élément recherché est plus petit, on ne garde que la partie gauche du tableau. Si l'élément recherché est plus grand, on ne garde que la partie droite du tableau. On répète l'opération jusqu'à trouver l'élément recherché ou jusqu'à ce qu'il n'y ait plus qu'un élément dans le tableau.  
La dichotomie est un exemple typique

```python
def recherche_dichotomique(L, x):
    if len(L) == 0:
        return False
    if len(L) == 1:
        return L[0] == x
    if L[len(L)//2] == x:
        return True
    if L[len(L)//2] > x:
        return recherche_dichotomique(L[:len(L)//2], x)
    return recherche_dichotomique(L[len(L)//2:], x)
```

Il y a plein de manières d'optimiser la recherche dichotomique dans une liste, notamment en utilisant des indices plutôt que des tranches de liste, ce qui a une complexité caché assez importante.


# Important pour le BAC

Au bac, le plus important est de savoir déterminer la complexité d'un algorithme. Pour cela, il faut savoir repérer les boucles et les appels récursifs.  
Pour les boucles, il faut savoir combien de fois on fait le tour de la boucle, identifier si il y a des boucles imbriquées et si oui, combien de fois on fait le tour de la boucle intérieure à chaque fois (ce nombre peut varier).

### Exemple 1
Pour la fonction tri 
```python
def tri(tab):
    for i in range(1, len(tab)):
        for j in range(len(tab)-i):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
```
La question est : combien d'échanges effectue la fonction python pour trier un tableau de 10 éléments dans le pire des cas ?

*Pour éviter de répéter `len(tab)` à chaque fois, dans la suite on considère que `n=len(tab)`.*
À première vue le code peut faire peur mais il faut juste le décomposer.  
On a une première boucle `for` qui va de 1 à `n-1`. On a donc `n-1` tours de boucle.  
À chaque tour de boucle, on a une boucle `for` qui va de 0 à `n-i`. On a donc `n-i` tours de boucle.
On a donc `n-1` tours de boucle extérieure et `n-i` tours de boucle intérieure à chaque tour de boucle extérieure. Au total on a donc $\sum_{i=1}^{n-1} n-i$ fois le `if` qui est exécuté.  
$\sum_{i=1}^{n-1} n-i = \sum_{i=1}^{n-1} n - \sum_{i=1}^{n-1} i = (n-1)n - \frac{(n-1)n}{2} = \frac{n(n-1)}{2}$  
Dans le pire des cas on peut supposer que `tab[j] > tab[j+1]` est toujours vrai, donc pour une liste de 10 éléments, on a $\frac{10\times9}{2} = 45$ échanges.

#### Remarque :
`tab[j] > tab[j+1]` est toujours vrai si la liste est triée dans l'ordre décroissant au départ.

#### Explications mathématiques :
Le symbole $\sum$ est la somme des termes d'une suite. Si la notation est trop compliqué on peut aussi l'écrire : $(n-1) + (n-2) + (n-3) + ... + 1$.  
Si on retourne la somme, on a : $1 + 2 + 3 + ... + (n-2) + (n-1)$. On reconnaît une suite arithmétique de raison 1. La somme des $n$ premiers termes d'une suite arithmétique de raison $r$ vaut $\frac{n(n+1)}{2}$. Or ici on a seulement la somme des $n-1$ premiers termes. Notre somme vaut donc bien $\frac{n(n-1)}{2}$.


On peut également vous demander de compléter un code à trous.

### Exemple 2
```python
def moyenne(tableau):
    total = ...
    for valeur in tableau:
        total = total + valeur
    return total / ...
```
Pour cet exemple il faut juste se souvenir de comment faire la moyenne d'une liste. C'est la somme des éléments divisée par le nombre d'éléments. Une somme commence à 0 et on a autant d'éléments que la longueur de la liste. On a donc `total = 0` et `return total / len(tableau)`.

Enfin, on peut vous poser des questions de cours à appliquer.

### Exemple 3
> Avec un algorithme de recherche par dichotomie, combien d'étapes sont nécessaires pour déterminer que 35 est présent dans le tableau [1, 7, 12, 16, 18, 20, 24, 28, 35, 43, 69] ?

Il suffit alors de faire une dichotomie "à la main" pour trouver la réponse. À la première étape on coupe la liste en deux et on regarde si 35 est plus petit ou plus grand que 20. On voit que 35 est plus grand que 20 donc on ne garde que la partie droite de la liste. On recommence avec la liste [24, 28, 35, 43, 69]. On coupe la liste en deux et on regarde si 35 est plus petit ou plus grand que 35. On voit que 35 est égal à 35 donc on a trouvé. On a donc fait deux étapes.

> Pour pouvoir appliquer l'algorithme de recherche dichotomique dans une liste, quelle précondition est vraie ?
> - [ ] La liste doit être triée
> - [ ] La liste ne doit pas comporter de doublons
> - [ ] La liste doit comporter uniquement des entiers positifs
> - [ ] La liste doit être de longueur inférieure à 1024

Cours pur : Pour appliquer l'algorithme de recherche dichotomique, il faut que la liste soit triée.
