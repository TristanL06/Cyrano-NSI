# Logiciel de gestion de bibliothèques

Vous êtes un ingénieur en informatique et vous devez faire un logiciel qui permettre à des bibliothèques de gérer leur activité au quotidien.

Le cahier des charges suivant est progressif et suit les différentes étapes de création du logiciel et il est conseillé de les suivre dans l'ordre. Les élèves auront 1h30 pour faire le plus possible du cahier des charges. Ce qui n'aura pas été réalisé dans le temps impartis pourra être réalisé en travail personnel, noté en TPA.  
**Il n'est ni possible ni demandé de terminer cet exercice en 1h30**, la réflexion et les solutions trouvées seront le seul critère de notation.

__Le client :__
Le client, représenté par monsieur Masseri, est la bibliothèque François Bourdel de Nice. Elle souhaite se doter d'un logiciel pour gérer ses livres, ses employés et ses clients.

Dans ce but elle souhaite une application contenant :
- Un système d'enregistrement des livres
- Un système d'inventaire
- Un import des livres depuis un format CSV
- Un import de livres depuis un format Json
- Un export des livres vers un format CSV
- Un export de livres vers un format Json
- Récupération des informations depuis l'api du site babelio (enregistrement d'un livre complet depuis son numéro ISBN)

- Créer un système de gestion de clients
- ajouter des forfaits différents
- ajouter un système de prêt de livres
- Faire des statistiques sur les emprunts de livre
- importer les nombres de livres prêtables selon forfait depuis un fichier CSV ou Json séparé
- ajouter un système de réduction pour les forfaits

- Ajouter des DVD
- Ajouter des Jeux (PS5, Xbox, switch...)

- Ajouter des bibliothécaires
- Ajouter des salles réservables
- Ajouter un système de réservation de salles
- Mettre à jour le fichier des autorisations d'emprunt pour inclure des durées mensuelles de réservation

- Générer une carte de bibliothèque au format PNG
- Ajouter une Photo aux adhérents
- Ajouter une photo aux bibliothécaires
- Générer un badge d'employé

L'interface graphique n'est pas demandée mais pourra être évaluée par un TPA si elle est fournie.
Il est recommandé d'utiliser les bibliothèques suivantes :
```python
import json
import requests
from datetime import datetime
```

Il est très fortement recommandé d'utiliser la Programmation Orientée Objet. Vous pouvez créer et utiliser tous les fichiers de tests et toutes les ressources à disposition.
