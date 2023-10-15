# Chapitre 3 : Les fichiers

L'intérêt de l'informatique est en partie de pouvoir lire et écrire des fichiers. Que ce soit pour enregistrer des informations de connexion, des données météo ou des messages il faut pouvoir écrire dans des fichiers. Pour traiter des données, récupérer des informations et automatiser certaines tâches.

## Jouer avec les fichiers locaux

La première étape consiste à utiliser des fichiers locaux pour faire tout ça. **Dans la suite le fichier que l'on utilise doit être dans le même fichier que le script python**.

On peut globalement faire 3 choses avec les fichiers :
- les lire
- Y écrire quelque chose
- Y ajouter quelque chose

### Lire un fichier
Pour lire un fichier il faut utiliser la fonction par défaut `open` de python qui prend en paramètres le nom du fichier et le mode d'ouverture, sous forme de string.
Pour ouvrir le fichier `test.txt` en mode lecture (`r`) on peut utiliser le code suivant :
```python
file = open("test.txt", "r")
```
La variable `file` contient alors un objet représentant le fichier, que l'on peut lire en utilisant la méthode `read()` ou `readlines()`.
```python
file = open("test.txt", "r")
data = file.read()
file.close()

print(data)
```
Ce code affiche le texte présent dans le fichier. **Il est important de toujours refermer le fichier** pour éviter des erreurs, surtout lors de l'écriture.

### Écrire dans un fichier
Pour écrire dans un fichier il suffit d'ouvrir le fichier en mode écriture (`w`) et d'utiliser la méthode `write()` :
```python
file = open("test.txt", "w")
file.write("Hello World")
file.close()
```
On n'oublie pas de bien refermer le fichier.
La méthode `write(str)` renvoie le nombre d'octets enregistrés dans le fichier.

### Ajouter à un fichier
Dans de très nombreux cas on veut garder toutes les valeurs déjà présentes dans le fichier et y en ajouter une. On la rajoute souvent avec un retour à la ligne (`\n`) après, pour les différencier les unes des autres.
Ce code permet à l'utilisateur de rentrer du texte qui sera sauvegardé dans un fichier. On remarquera l'utilisation du mode d'ajout (`a`) pour ajouter le texte au fichier :
```python
a = ""
while a != "q":
	a = input("Entrez quelque chose à sauvegarder (q pour quitter) =>")
	file = open("sauvegarde.txt", "a") # on ouvre le fichier en mode ajout
	file.write(a) # on ajoute a
	file.close() # on n'oublie pas de fermer le fichier
print("fin d'exécution du code")
```


## Les fichiers CSV

Les fichiers csv (comma-separated values) sont des fichiers pratiques pour stocker des informations de manière légère. Pour ce faire on peut imaginer un tableau dans lequel on a des informations à propos d'élèves :

| Prénom   | Nom        | Sortilèges | Potions | Astronomie | Métamorphose |
|----------|------------|------------|---------|------------|--------------|
| Elara    | Silverwood | 95         | 88      | 78         | 92           |
| Cedric   | Thornfield | 80         | 75      | 60         | 70           |
| Isabella | Nightshade | 90         | 85      | 70         | 88           |
| Orion    | Blackwood  | 85         | 92      | 75         | 84           |

ces informations peuvent facilement être enregistrées dans un fichier CSV : 
```csv
Prénom, Nom, Sortilèges, Potions, Astronomie, Métamorphose
Elara, Silverwood, 95, 88, 78, 92
Cedric, Thornfield, 80, 75, 60, 70
Isabella, Nightshade, 90, 85, 70, 88
Orion, Blackwood, 85, 92, 75, 84
```
Chaque ligne est séparée de la suivante par un retour à la ligne (`\n`) et chaque colonne est séparée de la suivante pas une virgule.  

> On remarque que la première ligne contient les noms des colonnes, ce n'est pas obligatoire mais c'est une bonne pratique. On peut également avoir plusieurs lignes d'explications sur le fichier (voir exercice 6 du TD)

On peut alors récupérer les informations contenues dans le fichier `élèves.csv` et les utiliser :
```python
file = open("élèves.csv", "r")
data = file.read()
file.close()

lignes = data.split("\n") # on découpe le contenue aux retours à la ligne
for ligne in lignes:
	ligne = ligne.split(",") # on découpe chaque ligne au niveau des virgules
	if ligne[0] == Cedric:
		print(ligne[4])
```
Ce programme permet d'afficher la note d'Astronomie de tous les élèves qui s'appellent Cédric.
## Bonus :
Il existe une notation plus compacte pour travaille avec des fichiers, elle utilise les indentations :
```python
with open("file.txt","r") as file:
	data = file.read()
print(data)
```
Le mot-clé `with` permet de définir l'objet représentant le fichier dans l'indentation et de fermer automatiquement le fichier lorsque l'on sort de l'indentation. Cette notation peut être source d'incompréhension, c'est à vous de voir laquelle vous préférez et vous trouvez la plus claire.

### Format JSON (Hors programme)
Le format JSON (JavaScript Object Notation) est un format de fichier très utilisé pour stocker des données. Il est très proche de la notation des dictionnaires python :
```json
{
	"Prénom": "Elara",
	"Nom": "Silverwood",
	"Sortilèges": 95,
	"Potions": 88,
	"Astronomie": 78,
	"Métamorphose": 92
}
```
On peut facilement convertir un dictionnaire python en fichier JSON :
```python
import json

dico = {
	"Prénom": "Elara",
	"Nom": "Silverwood",
	"Sortilèges": 95,
	"Potions": 88,
	"Astronomie": 78,
	"Métamorphose": 92
}
with open("élève.json", "w") as file:
	json.dump(dico, file)
```
Et on peut facilement convertir un fichier JSON en dictionnaire python :
```python
import json

with open("élève.json", "r") as file:
	dico = json.load(file)
print(dico)
```
Dans ces deux cas on utilise la notation avec `with` pour ouvrir et fermer le fichier automatiquement. On utilise également la bibliothèque `json` pour convertir le dictionnaire en fichier JSON et inversement.
La fonction `dump` permet de convertir un dictionnaire en fichier JSON et la fonction `load` permet de convertir un fichier JSON en dictionnaire.

La notation JSON est très utilisée pour stocker et transmettre des données. On l'utilise dans de grand nombres d'API (Application Programming Interface) pour transmettre des données entre un serveur et un client. On l'utilise également pour stocker des données dans des bases de données NoSQL (Not Only SQL) comme MongoDB.
Pour apprendre à manipuler les fichiers JSON n'hésitez pas à bidouiller en convertissant des dictionnaires de plus en plus complexes en fichier JSON et inversement. Vous pouvez utiliser le site [jsonviewer](https://jsonformatter.org/json-viewer) pour explorer un fichier JSON.
