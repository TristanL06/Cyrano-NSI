**Sommaire du cours**  
[Partie I : Architecture d'un ordinateur](#architecture-de-von-neumann)  
[Partie II : Utilisation de Linux](#linux-en-lignes-de-commandes)

# Architecture de Von Neumann

## Introduction
L'architecture de Von Neumann est un modèle d'architecture de calculateur. Elle a été proposée par John von Neumann en 1945. Elle est utilisée dans la plupart des ordinateurs actuels.

## Architecture
L'architecture de Von Neumann est composée de 4 parties :
- l'unité de calcul et de traitement (CPU)
- la mémoire
- des bus
- les périphériques d'entrée/sortie (clavier, souris, écran, etc...)

Tous les composants sont reliés par des bus de données. Les bus de données sont un ensemble de fils électriques qui permettent de transmettre des données entre les différents composants. Les bus sont synchronisés par une horloge, qui envoie un signal à intervalles réguliers pour synchroniser les composants.

![Architecture de Von Neumann](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Von_Neumann_Architecture.svg/1200px-Von_Neumann_Architecture.svg.png)

## Unité de calcul et de traitement (CPU)
L'unité de calcul et de traitement (CPU) est l'unité centrale de l'ordinateur. Elle est composée de 3 parties :
- l'unité arithmétique et logique (ALU)
- l'unité de contrôle (CU)
- les registres

### La mémoire
La mémoire est un composant qui permet de stocker des données. Elle est composée de plusieurs parties :
- la mémoire vive (RAM)
- la mémoire morte (ROM)

#### La mémoire vive (RAM)
La mémoire vive (RAM) est une mémoire volatile, c'est-à-dire que les données sont perdues quand l'ordinateur est éteint. Elle est utilisée pour stocker les programmes et les données en cours d'utilisation.

#### La mémoire morte (ROM)
La mémoire morte (ROM) est une mémoire non volatile, c'est-à-dire que les données ne sont pas perdues quand l'ordinateur est éteint. Elle est utilisée pour stocker les programmes et les données qui ne changent pas.

### Les bus
Les bus sont des ensembles de fils électriques qui permettent de transmettre des données entre les différents composants.

### Les périphériques d'entrée/sortie (clavier, souris, écran, etc...)
Les périphériques d'entrée/sortie permettent d'entrer des données dans l'ordinateur (clavier, souris, etc...) ou de sortir des données de l'ordinateur (écran, imprimante, etc...).

## Fonctionnement
L'ordinateur exécute un programme en plusieurs étapes :
1. le programme est chargé dans la mémoire vive
2. l'unité de contrôle (CU) lit les instructions du programme dans la mémoire vive
3. l'unité de contrôle (CU) envoie les instructions à l'unité arithmétique et logique (ALU)
4. l'unité arithmétique et logique (ALU) exécute les instructions
5. l'unité arithmétique et logique (ALU) envoie les résultats à la mémoire vive
6. l'unité de contrôle (CU) lit les résultats dans la mémoire vive
7. l'unité de contrôle (CU) envoie les résultats à l'unité arithmétique et logique (ALU)
8. l'unité de contrôle (CU) lit les instructions suivantes dans la mémoire vive et recommence à l'étape 3



# Linux en lignes de commandes

## Introduction
Linux est un système d'exploitation libre et gratuit. Il est utilisé sur la plupart des serveurs web et sur la plupart des smartphones (Android).  
Il est très courant de devoir utiliser un serveur Linux en lignes de commandes, que ce soit pour installer un serveur web, un serveur de base de données, un serveur de fichiers, etc... Il est donc utile de savoir utiliser les commandes de base de Linux.  
Le système de fichiers de Linux est organisé comme celui de Windows, avec des dossiers et des fichiers. On peut le représenter sous forme d'arborescence, avec un dossier racine `/` et des sous-dossiers. Chaques dossiers peut contenir des fichiers et d'autres dossiers.

## Organisation des fichiers et vocabulaire
Le dossier dans lequel on se trouve est appelé le dossier **courant**.  
Le dossier "au-dessus" dans l'arborescence est appelé le dossier **parent**.  

Il y a deux manières d'accéder à une ressource (fichier ou dossier), en utilisant un chemin absolu ou un chemin relatif.  
Le chemin absolu est le chemin complet depuis la racine `/`. Par exemple, le chemin absolu du dossier `cyrano` est `/home/pi/Documents/cyrano/`.  
Le chemin relatif est le chemin depuis le dossier courant. Par exemple, si le dossier courant est `/home/pi/Documents/`, le chemin relatif du dossier `cyrano` est `cyrano/`.

## Commandes de base

### `tree`
La commande `tree` permet d'afficher l'arborescence du système de fichiers. Par exemple, pour afficher l'arborescence du dossier `/home/pi/Documents/cyrano/`, on peut taper la commande suivante :
```bash
$ tree /home/pi/Documents/cyrano/
/home/pi/Documents/cyrano/
├── consignes
│   ├── consignes.txt
│   └── mistery.py
├── alexandre
├── john
├── kamel
├── marlon
└── maxence
4 directories, 0 files
```
> Pour installer la commande `tree`, il faut taper la commande `sudo apt install tree`, elle est installée par défaut sur le serveur de test utilisé.

`tree` permet d'afficher l'arborescence du dossier courant si aucun chemin n'est précisé.

### `ls`
La commande `ls` permet de lister les fichiers et dossiers présents dans le dossier courant.
```bash
$ ls
alexandre  john  kamel  marlon  maxence
```
On peut ajouter des options à la commande `ls` pour modifier son comportement. Par exemple, l'option `-l` permet d'afficher plus d'informations sur les fichiers et dossiers listés.
```bash
$ ls -l
total 20
drwxr----- 2 alexandre cyrano 4096 Jan 20 10:17 alexandre
drwxr----- 2 john      cyrano 4096 Jan 20 10:15 john
drwxr----- 2 kamel     cyrano 4096 Jan 20 10:18 kamel
drwxr----- 2 marlon    cyrano 4096 Jan 20 10:18 marlon
drwxr-xr-x 4 maxence   cyrano 4096 Jan 23 20:18 maxence
```
On peut aussi combiner plusieurs options. Par exemple, l'option `-a` permet d'afficher les fichiers et dossiers cachés, et l'option `-h` permet d'afficher les tailles des fichiers et dossiers en unités lisibles par un humain.
```bash
$ ls -la
total 28
drwxr-xr-x 7 root      root   4096 Jan 20 10:18 .
drwxr-xr-x 3 pi        pi     4096 Jan 20 10:03 ..
drwxr----- 2 alexandre cyrano 4096 Jan 20 10:17 alexandre
drwxr----- 2 john      cyrano 4096 Jan 20 10:15 john
drwxr----- 2 kamel     cyrano 4096 Jan 20 10:18 kamel
drwxr----- 2 marlon    cyrano 4096 Jan 20 10:18 marlon
drwxr-xr-x 4 maxence   cyrano 4096 Jan 23 20:18 maxence
```

imaginons que l'on ait cette arborescence :
```bash
.
├── test
└── test.txt
```
La commande `ls` affiche les fichiers et dossiers présents dans le dossier courant :
```bash
$ ls
test  test.txt
```
La commande `ls -l` affiche plus d'informations sur les fichiers et dossiers présents dans le dossier courant :
```bash
$ ls -l
total 4
drwxr-xr-x 2 tristan tristan 4096 Jan 31 08:55 test
-rw-r--r-- 1 tristan tristan    0 Jan 31 08:55 test.txt
```
Décortiquons un peu ce résultat :  
`total 4` : il y a 4 blocs de 1024 octets dans le dossier courant.  
Ensuite chaque ligne correspond à un fichier ou un dossier. Chacune de ces lignes est composée des mêmes informations :
- 1 caractère indiquant le type de fichier (d pour dossier, - pour fichier)
- 9 caractères indiquant les droits d'accès au fichier (3 caractères pour le propriétaire, 3 caractères pour le groupe, 3 caractères pour les autres). Les droits d'accès sont représentés par les caractères suivants :
  - r : lecture
  - w : écriture
  - x : exécution
  - \- : pas de droit
- le nombre de liens vers le fichier
- le nom du propriétaire du fichier
- le nom du groupe du fichier
- la taille du fichier en octets
- la date de dernière modification du fichier
- le nom du fichier


### `cd`
La commande `cd` permet de changer de dossier courant. Par exemple, pour aller dans le dossier `maxence`, on peut taper la commande suivante :
```bash
$ cd maxence
```

### `pwd`
La commande `pwd` permet d'afficher le chemin absolu du dossier courant. Par exemple, si on est dans le dossier `maxence`, on peut taper la commande suivante :
```bash
$ pwd
/home/pi/Documents/cyrano
$ cd maxence/
$ pwd
/home/pi/Documents/cyrano/maxence
```
Pour remonter dans le dossier parent, on peut utiliser la commande `cd ..` :
```bash
$ cd ..
$ pwd
/home/pi/Documents/cyrano
```

### `mkdir`
La commande `mkdir` permet de créer un dossier. Par exemple, pour créer un dossier `test` dans le dossier courant, on peut taper la commande suivante :
```bash
$ ls
alexandre  john  kamel  marlon  maxence
$ mkdir test
$ ls
alexandre  john  kamel  marlon  maxence  test
```

### `touch`
La commande `touch` permet de créer un fichier vide. Par exemple, pour créer un fichier `test.txt` dans le dossier courant, on peut taper la commande suivante :
```bash
$ ls
alexandre  john  kamel  marlon  maxence  test
$ touch test.txt
$ ls
alexandre  john  kamel  marlon  maxence  test  test.txt
```

### `rm`
La commande `rm` permet de supprimer un fichier. Par exemple, pour supprimer le fichier `test.txt` dans le dossier courant, on peut taper la commande suivante :
```bash
$ ls
alexandre  john  kamel  marlon  maxence  test  test.txt
$ rm test.txt
$ ls
alexandre  john  kamel  marlon  maxence  test
```

### `rmdir`
La commande `rmdir` permet de supprimer un dossier vide. Par exemple, pour supprimer le dossier `test` dans le dossier courant, on peut taper la commande suivante :
```bash
$ ls
alexandre  john  kamel  marlon  maxence  test
$ rmdir test
$ ls
alexandre  john  kamel  marlon  maxence
```

Si le dossier n'est pas vide, la commande `rmdir` ne fonctionne pas. Il faut utiliser la commande `rm -r` (remove recursive) pour supprimer un dossier et son contenu. Par exemple, pour supprimer le dossier `test` dans le dossier courant, on peut taper la commande suivante :
```bash
$ ls
alexandre  john  kamel  marlon  maxence  test
$ rm -r test
$ ls
alexandre  john  kamel  marlon  maxence
```

### `cp`
La commande `cp` permet de copier un fichier ou un dossier. Par exemple, pour copier le fichier `test.txt` dans le dossier courant, on peut taper la commande suivante :
```bash
$ ls
alexandre  john  kamel  marlon  maxence  test.txt
$ cp test.txt test2.txt
$ ls
alexandre  john  kamel  marlon  maxence  test.txt  test2.txt
```
> À noter que si le fichier `test2.txt` existe déjà, il sera écrasé par la copie de `test.txt`.

### `mv`
La commande `mv` permet de déplacer un fichier ou un dossier. Par exemple, pour déplacer le fichier `test.txt` dans le dossier courant, on peut taper la commande suivante :
```bash
$ ls
alexandre  john  kamel  marlon  maxence  test.txt
$ mv test.txt test2.txt
$ ls
alexandre  john  kamel  marlon  maxence  test2.txt
```
> Il n'existe pas de commande pour renommer un fichier ou un dossier. Pour renommer un fichier ou un dossier, on peut utiliser la commande `mv` comme dans l'exemple ci-dessus.

### `cat`
La commande `cat` permet d'afficher le contenu d'un fichier. Par exemple, pour afficher le contenu du fichier `test.txt` dans le dossier courant, on peut taper la commande suivante :
```bash
$ cat test.txt
Hello world!
```

### `nano`
La commande `nano` permet d'éditer un fichier. Par exemple, pour éditer le fichier `test.txt` dans le dossier courant, on peut taper la commande suivante :
```bash
$ nano test.txt
```
> Pour quitter l'éditeur `nano`, il faut appuyer sur `Ctrl + O` pour enregistrer les modifications, puis `Ctrl + X` pour quitter l'éditeur.

## Droits d'accès
Les droits d'accès d'un fichier ou d'un dossier sont représentés par les caractères suivants :
- r : lecture
- w : écriture
- x : exécution
- \- : pas de droit

les droits d'accès sont représentés par un chiffre entre 0 et 7. On peut le calculer en considérant rwx comme un nombre binaire. Par exemple, rwx = 111 = 7, r-x = 101 = 5, etc...
Comme il y a 3 droits d'accès différents (propriétaire, groupe, autres), on a 3 chiffres entre 0 et 7 pour représenter les droits d'accès d'un fichier ou d'un dossier. Par exemple, rwxr-xr-x = 755, rw-r----- = 640, etc...

### `chmod`
La commande `chmod` permet de modifier les droits d'accès d'un fichier ou d'un dossier. Par exemple, pour donner tous les droits à tous les utilisateurs sur le fichier `test.txt` dans le dossier courant, on peut taper la commande suivante :
```bash
$ ls -l
-rw-r--r-- 1 tristan tristan    0 Jan 31 08:55 test.txt
$ chmod 777 test.txt
$ ls -l
-rwxrwxrwx 1 tristan tristan    0 Jan 31 08:55 test.txt
```
7 = 111 en binaire, donc rwx pour le propriétaire, le groupe et les autres.  
Si on veut donner tous les droits au propriétaire, mais seulement la lecture aux autres, on peut taper la commande suivante :
```bash
$ ls -l
-rwxrwxrwx 1 tristan tristan    0 Jan 31 08:55 test.txt
$ chmod 744 test.txt
$ ls -l
-rwxr--r-- 1 tristan tristan    0 Jan 31 08:55 test.txt
```

On peut aussi utiliser des lettres pour modifier les droits d'accès. Par exemple, pour donner tous les droits à tous les utilisateurs sur le fichier `test.txt` dans le dossier courant, on peut taper la commande suivante :
```bash
$ ls -l
-rw-r--r-- 1 tristan tristan    0 Jan 31 08:55 test.txt
$ chmod a+rwx test.txt
$ ls -l
-rwxrwxrwx 1 tristan tristan    0 Jan 31 08:55 test.txt
```
> a = all, u = user, g = group, o = others  
> \+ = add, - = remove, = set

Cet usage est moins courant et moins lisible que l'usage avec des chiffres, il n'est donc pas recommandé.

### `chown`
La commande `chown` permet de modifier le propriétaire d'un fichier ou d'un dossier. Par exemple, pour donner le fichier `test.txt` dans le dossier courant à l'utilisateur `tristan`, on peut taper la commande suivante :
```bash
$ ls -l
-rw-r--r-- 1 root root    0 Jan 31 08:55 test.txt
$ chown tristan test.txt
$ ls -l
-rw-r--r-- 1 tristan root    0 Jan 31 08:55 test.txt
```

## Utilisateurs et groupes (avancé)


### `chgrp`
La commande `chgrp` permet de modifier le groupe d'un fichier ou d'un dossier. Par exemple, pour donner le fichier `test.txt` dans le dossier courant au groupe `tristan`, on peut taper la commande suivante :
```bash
$ ls -l
-rw-r--r-- 1 tristan root    0 Jan 31 08:55 test.txt
$ chgrp cyrano test.txt
$ ls -l
-rw-r--r-- 1 tristan cyrano    0 Jan 31 08:55 test.txt
```

### `useradd`
La commande `useradd` permet de créer un utilisateur. Par exemple, pour créer un utilisateur `test`, on peut taper la commande suivante :
```bash
$ useradd test
```

### `passwd`
La commande `passwd` permet de changer le mot de passe d'un utilisateur. Par exemple, pour changer le mot de passe de l'utilisateur `test`, on peut taper la commande suivante :
```bash
$ passwd test
```

### `groupadd`
La commande `groupadd` permet de créer un groupe. Par exemple, pour créer un groupe `test`, on peut taper la commande suivante :
```bash
$ groupadd ecole
```

### `usermod`
La commande `usermod` permet de modifier les propriétés d'un utilisateur. Par exemple, pour ajouter l'utilisateur `test` au groupe `ecole`, on peut taper la commande suivante :
```bash
$ usermod -a -G ecole test
```

### `userdel`
La commande `userdel` permet de supprimer un utilisateur. Par exemple, pour supprimer l'utilisateur `test`, on peut taper la commande suivante :
```bash
$ userdel test
```

### `groupdel`
La commande `groupdel` permet de supprimer un groupe. Par exemple, pour supprimer le groupe `test`, on peut taper la commande suivante :
```bash
$ groupdel ecole
```
