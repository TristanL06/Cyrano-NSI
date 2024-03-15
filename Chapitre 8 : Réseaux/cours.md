# Chapitre 8 : Les Réseaux

## Introduction

Les réseaux informatiques sont des systèmes qui permettent la communication et le partage de données entre différents ordinateurs et dispositifs. Les réseaux peuvent être de différents types, tels que les réseaux locaux (LAN), les réseaux étendus (WAN), les réseaux privés virtuels (VPN) et les réseaux sociaux en ligne.

## Protocoles de communication

Les protocoles de communication sont les règles qui permettent aux ordinateurs de communiquer efficacement. Certains des protocoles les plus courants sont TCP/IP, HTTP, FTP, DNS et DHCP.

Le protocole historique est décrit par le modèle TCP/IP et date de l'ARPANET (réseau militaire américain). Dans ce réseau dynamique chaque machine a un identifiant unique (MAC) et une adresse (IP).  
![IP](https://raw.githubusercontent.com/TristanL06/Cyrano-NSI/main/Chapitre%208%20%3A%20R%C3%A9seaux/ressources/Untitled%201.png)  
Ce modèle a ensuite été supplanté par le modèle OSI, contenant 7 couches, chacune correspondant à une fonction précise.  
![Couches modèles OSI, TCP/IP](https://raw.githubusercontent.com/TristanL06/Cyrano-NSI/main/Chapitre%208%20%3A%20R%C3%A9seaux/ressources/Untitled%202.png)  
![Couches modèles OSI, TCP/IP](https://raw.githubusercontent.com/TristanL06/Cyrano-NSI/main/Chapitre%208%20%3A%20R%C3%A9seaux/ressources/Untitled%203.png)  

Pour être envoyée à travers le réseau une information est découpée en paquets de taille normalisée et chaque paquet remonte les différentes couches du modèle. Chaque couche lui rajoute un en-tête pour préciser des informations (encodage, destination, nombre maximum de connexions...)  
![exemple IPV6](https://raw.githubusercontent.com/TristanL06/Cyrano-NSI/main/Chapitre%208%20%3A%20R%C3%A9seaux/ressources/Untitled%204.png)

Le protocole IPV4 utilise 4 octets pour encoder toutes les adresses (192.168.1.48 par exemple). Depuis quelques années le nombre croissants d'appareils connectés au réseau oblige à augmenter le nombre d'adresses disponibles, c'est pour cela que le protocole IPV6 a été créé (il utilise 6 octets).

## Topologie des réseaux

La topologie d'un réseau est la façon dont les différents éléments du réseau sont connectés entre eux. Les topologies de réseau les plus courantes sont les topologies en étoile, en anneau, en bus et en maillage.
![réseau](image.png)

Les topologies en étoile sont les plus courantes, elles sont utilisées dans les réseaux locaux (LAN) et les réseaux étendus (WAN). Dans une topologie en étoile, chaque ordinateur est connecté à un concentrateur ou à un commutateur, qui est le point central du réseau. Les topologies en étoile sont faciles à installer et à gérer, mais elles peuvent être coûteuses à mettre en place.  
Les topologie en bus sont surtout utilisés dans les voitures ou les avions, où les ordinateurs sont connectés à un seul câble.  
Chaque topologie a ses avantages et ses inconvénients, et le choix de la topologie dépend des besoins spécifiques du réseau.

## Physiologie de réseau

La physiologie de réseau décrit la façon dont les différents éléments d'un réseau sont connectés et interagissent entre eux. Les éléments clés d'un réseau incluent les ordinateurs, les routeurs, les switches, les concentrateurs et les modems.

Les réseaux sont répartis en 4 catégories selon leur taille :
- PAN (Personnal Arena Network) Bluetooth, NFC, connexions à quelques mètres
- LAN (Local Arena Network) : wifi, connexion à l'intérieur d'un bâtiment
- MAN (Metropolitan Arena Network) : 4G, connexions au niveau d'une ville
- WAN (Wide Arena Network) : Connexion mondiale, internet

### **Les routeurs**
-   Chaque sous-réseaux est connecté à un ou plusieurs autres sous-réseaux. Les **routeurs** sont chargés du trafic, c'est à dire du routage des **paquets de données**.
-   Les données sont propagées de proche en proche et doivent trouver leur chemin vers le récepteur.
-   Tout le problème est de trouver un chemin entre l'émetteur et le récepteur.
-   Le routeur utilise une **table de routage,** c'est à dire un tableau d'adresses vers les sous-réseaux adjacents.
-   On ajoutera que tout les chemins ne vont pas avoir le même coût  
![réseau](https://github.com/TristanL06/Cyrano-NSI/raw/main/Chapitre%208%20:%20R%C3%A9seaux/ressources/Untitled.png)

Pour fonctionner les routeurs utilisent des **tables de routage**, qui indiquent quelle sortie (passerelle) du routeur un paquet doit emprunter s'il veut se rendre vers une adresse.  
Il existe toujours une sortie par défaut, pour que le paquet dont la destination n'est pas dans la table de routage aille vers un autre routeur pour trouver son chemin.  

![réseau](https://github.com/TristanL06/Cyrano-NSI/raw/main/Chapitre%208%20:%20R%C3%A9seaux/ressources/Untitled%205.png)  
Avec ce réseau on peut imaginer la table suivant pour le routeur R5 :
| Destination | Passerelle | Coût |
| :-: | :-: | :-: |
| \* | WAN 5 | 1 |
| 172.16.2.* | WAN 6 | 10 |

## Représentation sous forme de graphs

Les réseaux peuvent être représentés sous forme de graph, ce qui permet une visualisation facile des relations entre les différents éléments du réseau. Dans une représentation de graph de réseau, les nœuds représentent les ordinateurs et les dispositifs, tandis que les arcs représentent les connexions entre eux.


Les réseaux informatiques sont une partie importante de notre vie quotidienne, et comprendre les différents aspects des réseaux, tels que les protocoles de communication, la physiologie de réseau et la représentation sous forme de graph, est essentiel pour une utilisation efficace des réseaux.

## Construction d'une adresse IP V4

Une adresse IP est une suite de 4 octets (32 bits) qui permet d'identifier un ordinateur sur un réseau. Chaque octet est écrit en décimal et séparé par un point.
À la fin de l'adresse on peut ajouter un masque de sous-réseau, qui permet de déterminer le nombre de bits de l'adresse qui sont utilisés pour identifier le réseau. Pour cela on utilise une notation en CIDR (Classless Inter-Domain Routing) qui est une suite de l'adresse IP suivi d'un slash et du nombre de bits utilisés pour identifier le réseau.  
Par exemple, `192.168.1.48/24` signifie que les 24 premiers bits de l'adresse sont utilisés pour identifier le réseau. Si on décompose l'adresse en binaire on obtient :  
`11000000.10101000.00000001.00110000`  
`11000000.10101000.00000001` est l'adresse du réseau et `00110000` est l'adresse de l'ordinateur sur le réseau.  
Avec cette méthode on peut avoir jusqu'à 2^32 adresses de réseaux différentes, soit 4 294 967 296 adresses. Cependant on ne peut avoir que 2^8-2 machines sur un réseau (moins 2 car l'adresse de réseau et l'adresse de broadcast ne sont pas utilisables).
L'adresse de réseau est l'adresse dont tous les bits de l'adresse de l'ordinateur sont à 0, et l'adresse de broadcast est l'adresse dont tous les bits de l'adresse de l'ordinateur sont à 1 (ici respectivement 192.168.1.0 et 192.168.1.255).

### Classes d'adresses IP

Il existe 5 classes d'adresses IP, qui sont déterminées par les premiers bits de l'adresse. Cela permet de déterminer le nombre de bits utilisés pour identifier le réseau et le nombre de bits utilisés pour identifier l'ordinateur.

| Classe | 1ère adresse | dernière adresse | Nombre de réseaux | Nombre d'ordinateurs par réseau | Masque de sous-réseau |
| :-: | :-: | :-: | :-: | :-: |
| A | 0.0.0.0 | 126.255.255.255 | 126 | 16 777 214 | 255.0.0.0 |
| B | 128.0.0.0 | 191.255.255.255 | 16 384 | 65 534 | 255.255.0.0 |
| C | 192.0.0.0 | 223.255.255.255 | 2 097 152 | 254 | 255.255.255.0 |

Les classes D et E sont réservées à des usages spécifiques.

### Adresses de réseau privées
192.168.1.xxx est une adresse IP privée, utilisée pour les réseaux locaux comme les réseaux wifi domestiques.  
10.0.0.xxx est une autre adresse IP privée, utilisée pour les réseaux locaux.  
172.126.0.xxx à 172.126.255.xxx est une plage d'adresses IP privées, utilisée pour les réseaux locaux.
