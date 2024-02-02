# TD Linux

## Prérequis
Tous les exercices peuvent être réalisés sur un raspberry pi mis à dispositon par ssh.  
Pour y accéder, il faut ouvrir un terminal et taper la commande suivante :
```bash
ssh prénom@80.119.177.18 -p 8080
```
`prénom` doit être remplacé par votre prénom (tout en minuscule) et le mot de passe est votre date de naissance au format `JJMMAAAA`.  
Vous avez un accès complet à votre répertoire personnel. Celui-ci est au bout du chemin `/home/pi/Documents/cyrano/prénom/`.

## Exercice 1
1. Créer un répertoire `td1` dans votre répertoire personnel.
2. Créer un fichier `ex1.txt` dans le répertoire `td1`.
3. écrire dans le fichier `ex1.txt` le texte suivant :
```
Bonjour,
Je suis un fichier texte.
```
4. Afficher le contenu du fichier `ex1.txt` dans le terminal.
5. Créer un fichier `ex2.txt` dans le répertoire `td1`.
6. Copier le contenu du fichier `ex1.txt` dans le fichier `ex2.txt`.
7. Afficher le contenu du fichier `ex2.txt` dans le terminal.
8. supprimer le répertoire `td1` et son contenu.

## Exercice 2
1. Créer un répertoire `td2` dans votre répertoire personnel.
2. Créer un fichier `ex1.txt` dans le répertoire `td2`.
3. écrire dans le fichier `ex1.txt` le texte suivant :
```
Bonjour,
Je suis un fichier texte.
```
4. Modifier les droits du fichier `ex1.txt` pour que tout le monde puisse le lire.
5. Afficher le contenu du fichier `ex1.txt` dans le terminal.
6. Supprimer le répertoire `td2` et son contenu.

## Exercice 3
1. Créer un répertoire `td3` dans votre répertoire personnel.
2. Créer le fichier `script.sh` dans le répertoire `td3` avec le contenu suivant :
```bash
#!/bin/bash
echo "Bonjour, je suis un script"
```
3. Modifier les droits du fichier `script.sh` pour que seul le propriétaire puisse l'exécuter.
4. Exécuter le script `script.sh`.
5. Supprimer le répertoire `td3` et son contenu.

## Exercice 4
1. Dans le répertoire `cyrano`, quels sont les droits du répertoire `consignes` ?
2. Quelle commande aurait-on pu utiliser pour mettre les droits du répertoire `consignes` comme dans la question précédente ?
3. Si on veut que tout le monde puisse écrire dans le répertoire `consignes`, quelle commande peut-on utiliser ?
