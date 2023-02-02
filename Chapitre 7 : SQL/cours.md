# Chapitre 7 : Bases de données et SQL

Pour stocker des données la plupart du temps le format le plus optimisé est le *json*, en organisant les données sous forme de dictionnaires :
```json
{0:{"nom":"Dubois", "adresse":"6 rue du port", "numéro":"06 60 06 60 06"},
 1:{"nom":"Martin", "adresse":"47 avenue des champs", "numéro":"07 69 42 24 96"},
 2:{"nom":"Cresson", "adresse":"57 rue de vienne", "numéro":"06 19 91 19 92"}}
```

Il peut cependant être assez compliqué de récupérer les informations de manière efficace si le stockage n'a pas été prévu pour ça (par exemple, récupérer tous les numéros de téléphone commençant par `07` est long à calculer avec un grand nombre de données), c'est pour cela que le SQL a été inventé.

SQL (Structured Query Language) est un langage informatique qui permet de gérer les données dans une **base de données relationnelle**. Il est utilisé pour créer, modifier et interroger des bases de données.

Une base de données est un ensemble de données **organisées** de manière logique. Elle est généralement utilisée pour stocker des informations relatives à une entreprise, comme les clients, les produits, les commandes, etc. Il existe différents types de bases de données, mais les plus courantes sont les bases de données **relationnelles**, qui sont organisées sous forme de **tables**.

Une table est une collection de données organisées sous forme de **lignes** (enregistrement) et de **colonnes** (attributs). Chaque ligne d'une table correspond à un enregistrement, et chaque colonne correspond à un **champ**. Par exemple, dans une table "clients", les colonnes pourraient être "nom", "adresse" et "numéro de téléphone", et chaque ligne représenterait un client différent.

| id |   nom   |        adresse       |     numéro     |
|:--:|:-------:|:--------------------:|:--------------:|
|  0 |  Dubois |     6 rue du port    | 06 60 06 60 06 |
|  1 |  Martin | 47 avenue des champs | 07 69 42 24 96 |
|  2 | Cresson |   57 rue de vienne   | 06 19 91 19 92 |

*ici la table contient 3 enregistrements, on dit qu'elle est de cardinal 3*  

SQL permet de réaliser différentes opérations sur les tables d'une base de données, comme :

-   Sélectionner des données à partir d'une ou plusieurs tables (SELECT)
-   Insérer de nouvelles données dans une table (INSERT)
-   Modifier des données existantes dans une table (UPDATE)
-   Supprimer des données d'une table (DELETE)

Il est également possible de créer, supprimer et modifier les structures des tables avec les commandes SQL correspondantes :

-   CREATE TABLE pour créer une nouvelle table
-   ALTER TABLE pour modifier une table existante
-   DROP TABLE pour supprimer une table

On va maintenant créer une table de gestion d'actifs financiers.

On doit donc avoir une table avec des `idClient`, des `idStocks` et des `quantité` de stocks détenus. On considère que le tuple (idClient, idStock) est unique et constitue donc une clé.

**comptes**  
| idClient |   idStock   | quantité   |
|:--:|:-------:|:--------------------:|
| 104 | 97 | 21 |
| 122 | 97 | 47 |
| 104 | 54 | 57 |

Pour obtenir toutes les données on peut faire la commande  
```SQL
SELECT * FROM comptes
```

Pour avoir les Stocks et quantités concernant le client 104 on peut faire  
```SQL
SELECT idStock, quantité FROM comptes
WHERE idClient = 104
```

Si on veut ordonner la réponse par ordre décroissant des quantités :  
```SQL
SELECT idStock, quantité FROM comptes
WHERE idClient = 104
ORDER BY quantité DESC
```

Maintenant si on veut également stocker la valeur de chaque Stock on peut ajouter un attribut à la table :  

**comptes**  
| idClient |   idStock   | quantité   | valeurStock |
|:--:|:-------:|:--------------------:| :-: |
| 104 | 97 | 21 | 18 |
| 122 | 97 | 47 | 18 |
| 104 | 54 | 57 | 6  |  

Et là on remarque que la valeur du Stock 97 va être stockée 2 fois. Et plus largement un stock a une valeur unique, il n'y a donc aucun intérêt de le stocker à chaque client. Il devient donc intéressant de combiner plusieurs tables.

___

## Travailler avec plusieurs tables

Il est également possible de créer des relations entre les tables grâce aux clés étrangères, qui permettent de lier des données d'une table à des données d'une autre table.

On sépare donc la table précédente en deux :

**comptes**  
| idClient |   idStock   | quantité   |
|:--:|:-------:|:--------------------:|
| 104 | 97 | 21 |
| 122 | 97 | 47 |
| 104 | 54 | 57 | 

**bourse**  
| idStock | valeurStock |
|:-------:|:-----:|
| 97 | 18 |
| 54 | 6  |  

On voit bien ici que `idClient` est la clé primaire de la table `comptes` et `idStock` la clé primaire de la table `bourse`.
Mais `idStock` est une clé secondaire de la table `comptes`

Maintenant on peut "coller" les deux tables pour travailler dessus :

```SQL
SELECT * FROM
comptes
JOIN
bourse
ON comptes.idStock = bourse.idStock
```

Va renvoyer la "table" initiale.

| idClient |   idStock   | quantité   | valeurStock |
|:--:|:-------:|:--------------------:| :-: |
| 104 | 97 | 21 | 18 |
| 122 | 97 | 47 | 18 |
| 104 | 54 | 57 | 6  | 


Et on peut y appliquer tout ce que l'on a vu précédemment :

```SQL
SELECT idStock, quantité, valeurStock FROM
compte
JOIN
bourse
ON comptes.idStock = bourse.idStock
WHERE idClient = 104
ORDER BY valeurStock ASC
```

qui donne

| idStock   | quantité   | valeurStock |
|:--:|:-------:|:--------------------:|
| 54 | 57 | 6  | 
| 97 | 21 | 18 |


En utilisant SQL, il est possible de gérer efficacement les données d'une entreprise et de les rendre facilement accessibles pour une analyse et une exploitation ultérieure. C'est pourquoi SQL est un outil incontournable pour les professionnels de l'informatique et de la gestion de données.
