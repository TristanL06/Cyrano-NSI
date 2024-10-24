# Cours : Conversions de bases (binaire, décimal, hexadécimal)

## Introduction

En informatique, les données transitent et sont stockées sous forme de bits, des 0 et des 1. Lorsqu'un courant électrique circule dans un circuit, on dit que le bit est à 1, et lorsqu'il n'y a pas de courant, on dit que le bit est à 0. Les ordinateurs utilisent des circuits électroniques pour effectuer des calculs et traiter des données. Donc toutes les données doivent être converties en bits pour être traitées par un ordinateur. Pour organiser les bits on les regroupe en octets, qui sont des groupes de 8 bits. On travail avec plusieurs bases pour représenter les nombres en informatique :
- La base **décimale** (base 10) est celle que nous utilisons dans la vie de tous les jours, elle est composée de 10 chiffres (0 à 9).
- La base **binaire** (base 2) est utilisée par les ordinateurs, elle est composée de 2 chiffres (0 et 1).
- La base **hexadécimale** (base 16) est utilisée en informatique pour simplifier la lecture des nombres binaires, elle est composée de 16 chiffres (0 à 9 et A à F).  

Dans ce cours, nous allons apprendre à convertir des nombres d'une base à l'autre, entre binaire, décimal et hexadécimal.

> Pour représenter un nombre dans une base on utilise la notation suivante :  
$(x)_n$ où $x$ est le nombre à convertir et $n$ est la base dans laquelle on veut le convertir.  
Par exemple, $(1011)_2$ est le nombre 1011 en base 2, et $(11)_{10}$ est le nombre 11 en base 10.

## 1. Conversion entre le binaire et le décimal

### Explications mathématiques

La question qui s'est posée au début de l'informatique est de savoir comment représenter les nombres avec une suite de 0 et de 1, en faisant passer un courant ou non.  
On a donc décidé que pas de courant = 0 et courant = 1. Pour représenter 2 il a fallu ajouter un bit, ce qui nous donne 10 en binaire. C'est exactement le même principe que quand on passe de 9 à 10 en décimal, on ajoute un nouveau chiffre.  
On peut donc dire que le binaire est une base 2, car il n'y a que 2 chiffres possibles : 0 et 1.

En base 10, la formule mathématique pour représenter les nombres est la suivante :  
$(4537)_{10} = 4 * 10^3 + 5 * 10^2 + 3 * 10^1 + 7 * 10^0$

En binaire, la formule est la même, mais avec des puissances de 2 :  
$(1011)_2 = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0$

on multiplie chaque chiffre par la base élevée à la puissance correspondante, et on additionne le tout.  

### Conversion d'un nombre décimal en binaire

Pour convertir un nombre décimal en binaire, on divise le nombre par 2 et on note le reste. On recommence avec le quotient obtenu, jusqu'à obtenir un quotient nul. En lisant les restes de bas en haut, on obtient le nombre en binaire.

Exemple : Convertir $(13)_{10}$ en binaire
```
13 / 2 = 6 reste 1
6 / 2 = 3 reste 0
3 / 2 = 1 reste 1
1 / 2 = 0 reste 1
```
Donc $(13)_{10} = (1101)_2$

Cette méthode étant un peu lente, on peut utiliser une méthode plus rapide en utilisant des puissances de 2. On note les puissances de 2 (1, 2, 4, 8, 16...) de droite à gauche jusqu'à dépasser le nombre à convertir. On prend ensuite les puissances qui sont inférieures ou égales au nombre à convertir, et on les additionne pour obtenir le nombre en binaire.

Exemple : Convertir $(13)_{10}$ en binaire

1. on note les puissances de 2 de droite à gauche jusqu'à dépasser 13 :  
```
16  8  4  2  1
```

2. on compare la première puissance à 13, comme 16 est trop grand, on note 0, on passe à la suivante :  
```
16  8  4  2  1
 0  
```

3. 8 est plus petit que 13, on note 1, et on soustrait 8 à 13 :  
```
16  8  4  2  1
 0  1
```

4. On a fait 13-8=5. Donc on compare 4 à 5, 4 est plus grand que 5, on note 1 et on soustrait 4 :  
```
16  8  4  2  1
 0  1  1
```

5. On a fait 5-4=1. On compare 2 à 1, 2 est trop grand, on note 0 et on passe à 1 :  
```
16  8  4  2  1
 0  1  1  0
```

6. On a fait 1-0=1. On compare 1 à 1, ils sont égaux, on note 1 :  
```
16  8  4  2  1
 0  1  1  0  1
```

Donc $(13)_{10} = (1101)_2$


### Conversion d'un nombre binaire en décimal

Pour convertir un nombre binaire en décimal, on utilise la formule mathématique vue précédemment. On multiplie chaque chiffre par la puissance de 2 correspondante, et on additionne le tout.

Exemple : Convertir $(1101)_2$ en décimal
```
1 * 2^3 + 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 8 + 4 + 0 + 1 = 13
```
Donc $(1101)_2 = (13)_{10}$


Ce calcul étant assez long à écrire et assez compliqué à faire sans calculatrice, on peut utiliser une méthode plus rapide. On note les puissances de 2 de droite à gauche, comme à l'étape précédente et on écris le nombre binaire en dessous. On multiplie chaque chiffre par la puissance de 2 correspondante, et on additionne le tout.

Exemple : Convertir $(1101)_2$ en décimal
```
8  4  2  1
1  1  0  1
```

Je ne garde que les chiffre qui on un 1 en dessous, et je les additionne :
```
8 + 4 + 1 = 13
```
Donc $(1101)_2 = (13)_{10}$


## 2. Conversion entre le binaire et l'hexadécimal

### Explications mathématiques

L'hexadécimal est une base 16, donc il y a 16 chiffres possibles : 0 à F, d'après la table de conversion suivante :

| Décimal | Binaire | Hexadécimal |
|---------|---------|-------------|
| 0       | 0000    | 0           |
| 1       | 0001    | 1           |
| 2       | 0010    | 2           |
| 3       | 0011    | 3           |
| 4       | 0100    | 4           |
| 5       | 0101    | 5           |
| 6       | 0110    | 6           |
| 7       | 0111    | 7           |
| 8       | 1000    | 8           |
| 9       | 1001    | 9           |
| 10      | 1010    | A           |
| 11      | 1011    | B           |
| 12      | 1100    | C           |
| 13      | 1101    | D           |
| 14      | 1110    | E           |
| 15      | 1111    | F           |

### Conversion d'un nombre binaire en hexadécimal

Pour convertir un nombre binaire en hexadécimal, on découpe le nombre binaire en groupe de 4 bits en partant de la droite, et on les convertit en hexadécimal. Si le groupe le plus à gauche n'a pas 4 bits, on complète avec des 0 à gauche.

Exemple : Convertir $(101101101)_2$ en hexadécimal

On découpe en groupe de 4 bits en complétant à gauche :
```
0010 1101 1010
```

On convertit chaque groupe en décimal :
```
0010 1101 1010
 2    13   10
```

On convertit chaque décimal en hexadécimal d'après la table de conversion :
```
2    13   10
2     D    A
```

Donc $(101101101)_2 = (2DA)_{16}$

### Conversion d'un nombre hexadécimal en binaire

Pour convertir un nombre hexadécimal en binaire, on fait exactement l'inverse de la conversion précédente. On convertit chaque chiffre hexadécimal en binaire, et on les regroupe.

Exemple : Convertir $(2DA)_{16}$ en binaire

On convertit chaque chiffre en décimal d'après la table de conversion :
```
2    D    A
2    13   10
```

On convertit chaque décimal en binaire :
```
2    13   10
0010 1101 1010
```

Donc $(2DA)_{16} = (001011011010)_2$

> Comme en maths, quand un nombre commence par des 0, on peut les supprimer, donc $(001011011010)_2 = (1011011010)_2$


## 3. Conversion entre le décimal et l'hexadécimal

### Conversion d'un nombre décimal en hexadécimal

Pour convertir un nombre décimal en hexadécimal, on convertit le nombre décimal en binaire, puis le binaire en hexadécimal.

Exemple : Convertir $(49)_{10}$ en hexadécimal

1. On convertit $(49)_{10}$ en binaire :  
```
64  32  16  8  4  2  1
 0   1   1  0  0  0  1
```

2. On convertit $(110001)_2$ en hexadécimal :  
```
11  0001
3    1
```

Donc $(49)_{10} = (31)_{16}$

### Conversion d'un nombre hexadécimal en décimal

Pour convertir un nombre hexadécimal en décimal, on convertit le nombre hexadécimal en binaire, puis le binaire en décimal.

Exemple : Convertir $(7A)_{16}$ en décimal

1. On convertit $(7A)_{16}$ en binaire :  
```
 7    A
0111 1010
```

2. On convertit $(01111010)_2$ en décimal :  
```
64  32  16  8  4  2  1
 1   1   1  1  0  1  0
```

```
64 + 32 + 16 + 8 + 2 = 122
```

Donc $(7A)_{16} = (122)_{10}$
