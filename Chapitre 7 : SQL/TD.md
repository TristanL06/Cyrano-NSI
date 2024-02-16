Pour les exercices on pourra utiliser le site [https://applibot-api.onrender.com/cyrano/sql/](https://applibot-api.onrender.com/cyrano/sql/) pour utiliser les commandes.

# Exercice 1
Voici les deux tables disponibles par défaut dans le système de gestion fourni :
**users**
| id |   name   | age   |
|:--:|:-------:|:--------------------:|
| 1 | Alice | 25 |
| 2 | Bob | 22 |
| 3 | Charlie | 28 |
| 4 | David | 32 |
| 5 | Eve | 21 |

**products**
| id |   name   | price   |
|:--:|:-------:|:--------------------:|
| 1 | Laptop | 1000 |
| 2 | Mouse | 20 |
| 3 | Keyboard | 50 |
| 4 | Monitor | 300 |
| 5 | Printer | 150 |

1. Écrire une requête SQL pour obtenir le nom et l'âge de tous les utilisateurs.
2. Écrire une requête SQL pour obtenir le nom et le prix de tous les produits.
3. Écrire une requête SQL pour obtenir le nom et l'âge de tous les utilisateurs de plus de 25 ans.
4. Écrire une requête SQL pour obtenir le nom et l'âge de tous les utilisateurs de plus de 25 ans.
5. Afficher le nom et le prix de tous les produits triés par prix croissant.
6. Écrire une requête SQL pour obtenir le nom et le prix de tous les produits dont le prix est supérieur à 100.
7. Combien de produits coûtent plus de 100 ? Écrire une requête SQL pour obtenir le nombre de produits dont le prix est supérieur à 100. (on utilisera la fonction COUNT)

# Exercice 2
dans cet exercice on va mener de bout en bout la création d'une base de données, son exploitation et sa modification.  
On travaillera sur la base de données suivante :

**morceaux**
| id_morceau |   titre   | année   | id_interprete   |
|:--:|:-------:|:--------------------:| :-: |
| 1 | Like a Rolling Stone | 1965 | 1 |
| 2 | Respect | 1967 | 2 |
| 3 | Imagine | 1970 | 3 |
| 4 | Hey Jude | 1968 | 4 |
| 5 | Smells like teen spirit | 1991 | 5 |
| 6 | I want to hold your hand | 1963 | 4 |

**interpretes**
| id_interprete |   nom   | pays     |
|:--:|:-------:|:--------------------:|
| 1 | Bob Dylan | États-Unis |
| 2 | Aretha Franklin | États-Unis |
| 3 | John Lennon | Angleterre |
| 4 | The Beatles | Angleterre |
| 5 | Nirvana | Angleterre |

## Théorie
1. Quelle est la clé étrangère de la table `morceaux` ?
2. Écrire un schéma relationnel des tables `morceaux` et `interpretes`.

## Création de la base de données
1. Créer les tables `morceaux` et `interpretes` avec les attributs et les types de données correspondants.
2. Insérer les données dans les tables `morceaux` et `interpretes`.
3. Écrire une requête SQL pour être sur que les données ont bien été insérées.

## Exploitation de la base de données
1. Écrire une requête pour obtenir les titres des morceaux de l'intérprète ayant pour id 4.
2. Écrire une requête permettant d'afficher les noms des interprètes originaires d'Angleterre.
3. Exécuter la requête suivante :  
```SQL
SELECT titre, année FROM morceaux
ORDER BY année
```

    - Quel est le résultat de cette requête ?
    - À quoi sert ORDER BY ?
4. Écrire une requête permettant d'afficher les titres des morceaux par ordre alphabétique.
5. Écrire une requête permettant de lister les titres des interprètes venant des États-Unis.

## Modification de la base de données
1. Une erreur s'est glissée dans la table `morceaux`, l'année de sortie du morceau "Imagine" est en réalité 1971. Écrire une requête pour corriger cette erreur.
2. Écrire une requête pour ajouter l'interprète "The Who" originaire d'Angleterre à la table `interpretes`. Son id sera 6.
3. Écrire une requête pour ajouter le morceau "My Generation" sorti en 1965 à la table `morceaux`. Son id sera 7 et son interprète sera "The Who".
