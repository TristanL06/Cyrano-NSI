## TD guidé

#### Exercice 1 : Dichotomie
> Pour tout cet exercice on considère que la liste fournie en entrée est triée, il n'est donc pas nécessaire de le vérifier.
1. Écrire une fonction `dichotomie(liste, x)` prenant en entrée une liste triée et retournant `True` si  la liste contient l'élément `x`, `False` sinon.
2. Écrire une fonction récursive ``dichotomieR(liste, x)`` qui a la même utilité qu'à la question 1 en utilisant le principe de "diviser pour reigner".
3. L'utilisaton de la fonction `len()` et le *slicing* sont assez couteux algorithmiquement, imaginer donc une fonction récursive ``dichotomieR(liste, x, i, j)`` à partir de la réponse précendente qui n'utilise pas ces deux éléments.
