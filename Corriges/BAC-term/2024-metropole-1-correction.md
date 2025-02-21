# Correction NSI 2024 Métropole 1

## Exercice 1

1) La ligne 9 `s2.predecesseurs = []` met comme valeur de prédécesseurs de s2, ce qui veut dire que le site 2 n'a aucun autre site qui pointe vers lui.
2) 
```python
s4.predecesseurs = [(s1,1), (s2,2)]
s5.predecesseurs = [(s1,2), (s3,3), (s4,6)]
```
3) `s2.successeurs[1][1]` donne la seconde valeur du second tuple de la liste s2.successeurs. Dans le contexte, ça renvoie le nombre de connexions vers le site2 depuis le site 3, c'est à dire `5`.
4) Le site1 a une popularité de 6
5) 
```python
def calculPopularite(self):
    popularite = 0
    for site in self.predecesseurs:
        popularite += site[1]
    self.popularite = popularite
    seturn self.popularite
```

6) Ces manipulations correspondent à l'utilisation d'une file
7) Le code parcours tous les noeuds et les ajoute à la file, c'est un parcours en largeur d'abord.
8) `parcoursGraphe(s1)` renvoie `[s1, s3, s4, s5]`
9) 
```python
maxPopularite = site.popularite
siteLePlusPopulaire = site
```
10) la ligne `lePlusPopulaire(parcoursGraph(s1)).nom` renvoie `site3`
11) grâce à la coloration des noeuds du graph chaque noeud n'est visité qu'une seule et unique fois, on a donc une complexité entre une complexité linéaire et une complexité carrée. De même avec la fonction de recherche du minimum, qui n'évalue qu'une seule fois la valeur de chaque noeud, on a une complexité linéaire. Ces scripts semblent donc assez adaptés à des graphs plus grands.
