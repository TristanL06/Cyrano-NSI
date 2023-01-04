# Chapitre 5 : Les arbres

Les arbres ont de très nombreuses applications, y compris en mathématiques, dans l'industrie ou dans tous les systèmes d'organisation de fichiers.

![arbre](https://mermaid.ink/img/pako:eNpN0U1vhCAQBuC_YubEJprsbnvyVlf349BTe2q4TBRXExWD0KYx_veOChROPJkXGGCGUlYCUngqHJvoM-dDROONsePxcNiRMXbyuBBODjnh7FAwdvaxK8HHbgQfuxNeHB6EVwd7dJQkSZSFuISwHWYbihBX29SGW4h7iAfE0AvVY1vRvee1xEE3ohccUppWokbTaQ7xXqo7-VM2qPRanm2rUBr1bRdkOLUTh7Wy8GGh7c1YoRZF1WqpIK2xm0QMaLT8-B1KSLUywoXyFunpe58acfiS8t9i2-R9_6Ttr5Y_zwpyzA?type=png)  
*Ici on peut voir un arbre contenant 9 noeuds.*

les arbres **binaires** sont un exemple particulier d'arbre. Comme l'indique leur nom les arbres binaires ont au plus deux fils à chaque noeud. Et chaque noeud a exactement un père (sauf le noeud racine). Ils sont également orientés, l'ordre gauche/droite des fils est donc important.

![](https://mermaid.ink/img/pako:eNpNULsOgzAM_JXIUyvBD7AV6NipnaosbmIgEiQoj1YV4t8bCLT15Luz72RPIIwkKKC1OHbsVnPNYp0O2lCQx4TKQ6N6x1oMoqONqxInrVF-57Zdluc5K_9BlQBkMJAdUMkYOC0cB9_RQByK2EpqMPSeQ5akpjcv0aH1izxtESCCfW4LD3TKcViUmes52odRoqezVN5YKBrsHWWAwZvrWwsovA20D9UK483Dd2pEfTfmh2k1uaTvrE-aP3t4Xac?type=png)

## 📖 Définitions
### 💡 Noeud : 
Entité ayant exactement un noeud père (sauf la racine) et pouvant avoir au plus 2 noeuds fils.
### 💡 Racine : 
Noeud le plus haut de l'arbre, il n'admet aucun parent
### 💡Taille :
Nombre de noeuds d'un arbre
### 💡Profondeur :
Longueur du chemin le plus court vers la racine (la racine ayant une profondeur de 0)
### 💡Hauteur : 
Profondeur du noeud le plus profond (un arbre ayant uniquement une racine aura donc une profondeur de 0)
### Feuille :
Noeud sans fils
### Arbre binaire complet à gauche :
Arbre binaire dont tous les étages sont complets et dont toutes les feuilles sont tassées à gauche
### Valeur étiquetée :
Valeur éssociée à un noeud.

## Parcours des arbres

Il y a 4 manières de parcourir un arbre binaire :
- Parcours en largeur
- Parcours en profondeur **préfixe**
- Parcours en profondeur **infixe**
- Parcours en profondeur **postfix**

Dans la suite nous allons utiliser cet arbre comme exemple :  
![arbre démo](https://mermaid.ink/img/pako:eNpNkUFrhDAQhf9KmLKQBYXVrV3wVld3Tz21p5JL0KTKRiMxbinif2_M2K455X3z5mXCTFDqSkAKX4b3NfnIWUfceaX0cNjvyW4XIcgojRDECM4OxB4cEeSUxuh4RlA4EHmQILg4gC0vCK4OHD04IVgfJ2EYkmwrzusUXuRbUazjeHHZiusjs1R8GHIhib4R2SiVPiUygQBaYVreVO7702JjYGvRCgapu1ZC8lFZBgGWpNLfZc2NXcrTmg3laO5rQ8aHZmCwVGbWzS5-7CtuRVE1VhtIJVeDCICPVr__dCWk1oziz5Q33G2g_Xf1vPvU-qGFD3nDXfmVzb8DYnYa?type=png)


### Le parcours en largeur
l'arbre est parcourus étage par étage, la racine d'abord, puis les fils de la racines, puis les fils suivants...  
À chaque étage les noeuds sont parcourus de gauche à droite :  
![arbre largeur](https://raw.githubusercontent.com/TristanL06/Cyrano-NSI/main/Chapitre%205%20%3A%20Arbres%20binaires/ressources/largeur.gif)

On obtient donc \[00, 10, 12, 20, 21, 22, 23\] lors que l'on parcours de cet arbre **en largeur d'abord**

### Le parcours Préfixe
L'arbre est parcourus selon l'ordre *noeud*, *fils gauche*, *fils droit*  
![arbre prefixe](https://raw.githubusercontent.com/TristanL06/Cyrano-NSI/main/Chapitre%205%20%3A%20Arbres%20binaires/ressources/préfix.gif)

On obtient donc \[00, 10, 20, 21, 12, 22, 23\] lors que l'on parcours de cet arbre de manière **préfixe**

### Le parcours Infixe
L'arbre est parcourus selon l'ordre *fils gauche*, *noeud*, *fils droit*  
![arbre prefixe](https://raw.githubusercontent.com/TristanL06/Cyrano-NSI/main/Chapitre%205%20%3A%20Arbres%20binaires/ressources/infixe.gif)

On obtient donc \[20, 10, 21, 00, 22, 12, 23\] lors que l'on parcours de cet arbre de manière **infixe**

### Le parcours Postfixe
L'arbre est parcourus selon l'ordre *fils gauche*, *fils droit*, *noeud*  
![arbre prefixe](https://raw.githubusercontent.com/TristanL06/Cyrano-NSI/main/Chapitre%205%20%3A%20Arbres%20binaires/ressources/postfix.gif)

On obtient donc \[20, 21, 10, 22, 23, 12, 00\] lors que l'on parcours de cet arbre de manière **postfixe**


Résumé des méthodes de parcours des arbres :
![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Sorted_binary_tree_ALL.svg/562px-Sorted_binary_tree_ALL.svg.png)

## Cas Particuliers des arbres

### Les tas

Un **tas-max** est un arbre binaire complet à gauche dont chaque racine a une valeur étiquetée supérieure à celles de ses fils.  

Un **tas-min** est un arbre binaire complet à gauche dont chaque racine a une valeur étiquetée inférieure à celles de ses fils.  

L'arbre pris en exemple plus haut est un tas-min.

### Les arbres binaires de recherche

Les arbres binaires de recherche sont des arbres binaires étiquetés avec des clés tel que :
- les clés du sous-arbre de gauche sont inférieures ou égales à la clé de la racine,
- les clés du sous-arbre de gauche sont strictement supérieures à la clé de la racine,
- les deux sous-arbres sont eux-même des arbres binaires de recherche.

Cette structure d'arbres permet de diminuer la complexité temporelle de la recherche d'un élément.
