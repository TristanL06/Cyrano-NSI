# TD 5 : Algorithmique

## Exercice 1
Dans cet exercice on considère la somme des entiers k allant de 1 à n définie par $S_n = \sum_{k=1}^n k + (n - k)$.

1. recopier et tester le programme suivant :

```python
def somme(n):
    S = 0
    for k in range(1, n + 1):
        S = S + k + (n - k)
    return S
```
Quel est le résultat de somme(5) ? somme(10) ? somme(100) ?  

2. Ajouter une variable compteur et modifier le programme pour qu'il compte le nombre d'additions effectuées. Que remarquez-vous ?
3. Peut-on améliorer le programme pour qu'il effectue moins d'opérations ? Justifier votre réponse.
4. Écrire une fonction somme2(n) qui calcule la somme des entiers de 1 à n en effectuant le moins d'opérations possibles. Vérifier que somme2(100) donne le même résultat que somme(100).
5. Quelle est la complexité de somme2(n) ? Justifier votre réponse.

## Exercice 2
On considère la fonction suivante :

```python
def f(n):
    if n == 0:
        return 1
    else:
        return 2 * f(n - 1)
```

1. Que renvoie f(3) ? f(5) ? f(10) ? f(100) ?
2. Quelle est la complexité de f(n) ? Justifier votre réponse.
3. Peut-on remplacer la fonction f(n) par une opération mathématique ? Si oui, laquelle, et quelle serait alors la complexité ? Si non, pourquoi ?

## Exercice 3
on considère la fonction suivante :
```python
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return f(n - 1) + f(n - 2)
```
1. Calculer fibo(3), fibo(5), fibo(10).
2. Que se passe-t-il si on appelle fibo(100) ? Pourquoi ? (vous pouvez utiliser `ctrl + c` pour arrêter l'exécution du programme)
3. Ajoutez un print(n) au début de la fonction fibo(n) et testez fibo(5). Que remarquez-vous ?
4. Comment pourrait-on améliorer la fonction fibo(n) pour qu'elle soit plus efficace ? Justifier votre réponse.
5. Amélioer la fonction fibo(n) avec la méthode proposée à la question précédente. Tester fibo(100). Est-ce que cela fonctionne ?

## Exercice 4
On utilise le code suivant pour insérer un élément à sa place dans une liste triée :
```python
def inserer(L, x):
    i = 0
    while i < len(L) and L[i] < x:
        i = i + 1
    L.insert(i, x)
```

1. Tester la fonction. Quel est son intérêt par rapport à la fonction `append` ?
2. Quelle est la complexité de la fonction `inserer(L, x)` ? Justifier votre réponse.
3. Écrire une fonction `inserer2(L, x)` qui insère un élément dans une liste triée en effectuant le moins d'opérations possibles. Vérifier que `inserer2(L, x)` donne le même résultat que `inserer(L, x)`.
4. Quelle est la complexité de la fonction `inserer2(L, x)` ? Justifier votre réponse.

## Exercice 5
La sécurité des systèmes de chiffrement repose sur la difficulté à factoriser un grand nombre en produit de nombres premiers. Si on arrivait à décomposer une clé de chiffrement en facteurs de nombres premiers, on pourrait lire tous les messages chiffrés par cette clé.  
Un élève propose le programme suivant pour trouver les diviseurs d'un nombre n :
```python
def diviseurs(n):
    L = []
    for k in range(1, n + 1):
        if n % k == 0:
            L.append(k)
    return L
```

1. Tester la fonction. Expliquer la ligne `if n % k == 0:`.
2. Quelle est la complexité de la fonction `diviseurs(n)` ? Justifier votre réponse.
3. Les nombres cryptographiques sont des nombres extrêmement grands (de l'ordre de $10^{77}$ pour les plus petits). Sachant que votre ordinateur peut effectuer environ $10^9$ opérations par seconde, combien de temps faudrait-il pour factoriser un nombre cryptographique avec la fonction `diviseurs(n)` ?
4. Comment pourrait-on améliorer la fonction `diviseurs(n)` pour qu'elle soit plus efficace ? Justifier votre réponse. Écrire le programme correspondant.
5. Quelle est la complexité de la fonction `diviseurs2(n)` ? Justifier votre réponse.
6. Combien de temps faudrait-il pour factoriser un nombre cryptographique avec la fonction `diviseurs2(n)` ? Comparer avec la question 3.
7. Nos mots communications sont-elles en sécurité ?
