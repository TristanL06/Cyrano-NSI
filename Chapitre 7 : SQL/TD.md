Pour les exercices on pourra utiliser le site [https://applibot-api.onrender.com/cyrano/sql/](https://applibot-api.onrender.com/cyrano/sql/) pour utiliser les commandes.

# Exercice 1
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
