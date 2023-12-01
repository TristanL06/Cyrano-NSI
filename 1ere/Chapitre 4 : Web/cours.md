# Chapitre 5 : Les langages WEB

*pour ce cours il est conseillé d'utiliser un éditeur de texte comme [Visual Studio Code](https://code.visualstudio.com/)(recommandé) ou [Sublime Text](https://www.sublimetext.com/)*
*Il est également possible d'utiliser une version en ligne comme [VSC online](https://vscode.dev/) ou [codepen](https://codepen.io/)*

## Introduction
Le contenue affichée sur une page web est écrit dans un langage de balisage appelé HTML (HyperText Markup Language). Ce langage permet de définir la structure d'une page web, mais il ne permet pas de définir son style. Pour cela on utilise le CSS (Cascading Style Sheets) qui permet de définir le style d'une page web. Enfin, pour rendre une page web interactive, on utilise le JavaScript qui permet de définir le comportement d'une page web.

## HTML
Pour faire un site web, on utilise le HTML qui est un langage de balisage, c'est à dire qu'il permet de définir la structure d'une page web. Il est composé de balises qui sont des éléments délimités par des chevrons.  
Par exemple `<p>Je suis un paragraphe</p>` est une balise qui permet de définir un paragraphe.
Cette structure permet de mettre en page un document, mais également de récupérer de manière simple des informations sur une page web avec un bot.
Créons maintenant notre premier site web :
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mon premier site web</title>
</head>
<body>
    <h1>Mon premier site web</h1>
    <p>Je suis un paragraphe</p>
</body>
</html>
```
Ce code permet de créer une page web avec un titre et un paragraphe.
Détaillons un peu ce code :
- `<!DOCTYPE html>` permet de définir le type de document, ici un document HTML
- `<html>` permet de définir le début et la fin du document HTML
- `<head>` permet de définir l'entête du document, c'est à dire les informations qui ne seront pas affichées sur la page web
- `<title>` permet de définir le titre de la page web
- `<body>` permet de définir le corps du document, c'est à dire les informations qui seront affichées sur la page web
- `<h1>` permet de définir un titre de niveau 1 (le plus important)

On remarque que chaque balise ouvrante est fermée par une balise fermante. Il existe également des balises qui ne sont pas fermées comme `<br>` qui permet de faire un retour à la ligne, ou `<!DOCTYPE html>` qui commence le fichier.

Créez un nouveau projet et copiez le code ci-dessus dedans. Enregistrez le fichier sous le nom `index.html` et ouvrez le avec votre navigateur. Vous devriez voir apparaître votre page web.  
Allez maintenant dans le dossier contenant votre fichier HTML et ouvrez l'invite de commande. Tapez la commande `python -m http.server` (ou `python3 -m http.server` si ça ne fonctionne pas) et ouvrez votre navigateur à l'adresse `http://localhost:8000`. Vous devriez voir apparaître votre page web.  
Vous pouvez maintenant modifier votre fichier HTML et voir les modifications en temps réel en actualisant la page web. Par exemple, ajoutons une image :
```html 
<!DOCTYPE html>
<html>
<head>
    <title>Mon premier site web</title>
</head>
<body>
    <h1>Mon premier site web</h1>
    <p>Je suis un paragraphe</p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Smiley_head_happy.svg/1200px-Smiley_head_happy.svg.png" alt="Smiley">
</body>
</html>
```

Pour la suite il faut chercher les documentations en ligne, par exemple [w3schools](https://www.w3schools.com/html/default.asp) ou [MDN](https://developer.mozilla.org/fr/docs/Web/HTML). Beaucoup de choses sont faisables et c'est impossible de tout résumer ici.

## CSS

Le CSS (Cascading Style Sheets) est un langage qui permet de définir le style d'une page web. Il permet de définir la couleur, la taille, la police, la position, etc. de chaque élément d'une page web.
Pour utiliser le CSS, il faut d'abord créer un fichier CSS. Créez un fichier `style.css` dans le même dossier que votre fichier HTML.
Pour lier le fichier CSS à votre fichier HTML, il faut ajouter la balise `<link>` dans l'entête de votre fichier HTML :
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mon premier site web</title>
    <link rel="stylesheet" href="style.css"> <!-- On ajoute cette ligne here -->
</head>
<body>
    <h1>Mon premier site web</h1>
    <p>Je suis un paragraphe</p>
    <ul>
        <li>élément 1</li>
        <li>élément 2</li>
        <li>élément 3</li>
    </ul>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Smiley_head_happy.svg/1200px-Smiley_head_happy.svg.png" alt="Smiley">
</body>
</html>
```
Vous pouvez maintenant écrire du CSS dans votre fichier `style.css`. Par exemple, pour changer la couleur du titre, on peut écrire :
```css
h1 {
    color: red;
}
```
On peut également changer la couleur du texte du paragraphe, le centrer et changer la police d'écriture :
```css
p {
    color: blue;
    text-align: center;
    font-family: Arial;
}
```
On peut aussi changer la couleur du fond de la page :
```css
body {
    background-color: yellow;
}
```
On peut également modifier la taille de l'image :
```css
img {
    width: 100px;
}
```
Enfin on peut changer l'orientation de la liste :
```css
ul {
    list-style-position: inside;
}
```

CSS permet aussi de gérer des petits évènements, comme le survol d'un élément avec la souris. Par exemple, on peut changer la couleur du titre quand on passe la souris dessus :
```css
h1:hover {
    color: green;
}
```

Pour la suite il faut chercher les documentations en ligne, par exemple [w3schools](https://www.w3schools.com/css/default.asp) ou [MDN](https://developer.mozilla.org/fr/docs/Web/CSS). Beaucoup de choses sont faisables et c'est impossible de tout résumer ici.

## JavaScript

Le JavaScript est un langage de programmation qui permet de rendre une page web interactive. Il permet de définir le comportement d'une page web. Par exemple, on peut faire en sorte qu'un élément change de couleur quand on clique dessus, ou qu'un élément apparaisse quand on passe la souris dessus.
Pour utiliser le JavaScript, il faut d'abord créer un fichier JavaScript. Créez un fichier `script.js` dans le même dossier que votre fichier HTML.
Pour lier le fichier JavaScript à votre fichier HTML, il faut ajouter la balise `<script>` à la fin de la tête de votre fichier HTML :
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mon premier site web</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script> <!-- On ajoute cette ligne here -->
</head>
<body>
    <h1>Mon premier site web</h1>
    <p>Je suis un paragraphe</p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Smiley_head_happy.svg/1200px-Smiley_head_happy.svg.png" alt="Smiley">
</body>
</html>
```

On peut mettre un bouton sur la page web qui permet de changer le texte du paragraphe quand on clique dessus :
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mon premier site web</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
</head>
<body>
    <h1>Mon premier site web</h1>
    <p id="paragraphe">Je suis un paragraphe</p>
    <button onclick="changerTexte()">Changer le texte</button>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Smiley_head_happy.svg/1200px-Smiley_head_happy.svg.png" alt="Smiley">
</body>
</html>
```
```javascript
function changerTexte() {
    document.getElementById("paragraphe").innerHTML = "Je suis un autre paragraphe";
}
```
Ici on voit que le bouton possède un attribut `onclick` qui permet d'appeler une fonction JavaScript quand on clique dessus. Cette fonction permet de changer le texte du paragraphe en utilisant la fonction `getElementById` qui permet de récupérer un élément HTML en fonction de son `id`.


## Back
Tout ce qui a été vu précedemment étaient des fichiers envoyés à l'utilisateur et affichés sur sa machine. Cela permet de juste stocker les fichiers sur le serveur et faire tous les calculs sur la machine du client. Cela a l'avantage de ne pas avoir besoin d'un serveur très puissant, mais cela a l'inconvénient de ne pas pouvoir cacher le code source ou des informations sensibles comme des données personnelles ou des mots de passe.
Pour faire ça on utilise un serveur qui va faire les calculs et envoyer le résultat à l'utilisateur.
Dans ce cours nous allons voir comment faire un serveur en Python avec le module Flask. Ce n'est pas le langage le plus utilisé pour ça mais il est très simple à utiliser et permet de faire des choses très rapidement.

### Flask
Pour utiliser Flask il faut d'abord installer le module avec la commande `pip install Flask` (ou `pip3 install flask` si ça ne fonctionne pas).
Ensuite on peut créer un fichier `app.py` qui va contenir le code du serveur :
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world !"

if __name__ == "__main__":
    app.run(debug=True)
```
Ce code permet de créer un serveur qui affiche "Hello world !" quand on va sur la page d'accueil.
Pour lancer le serveur il faut exécuter le fichier `app.py` avec la commande `python app.py` (ou `python3 app.py` si ça ne fonctionne pas).
On peut maintenant aller sur la page d'accueil du serveur à l'adresse `http://localhost:5000` et on devrait voir apparaître "Hello world !".

Renvoyer du texte c'est bien, mais on peut faire mieux. On peut par exemple renvoyer du json :
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/bonjour")
def index():
    return jsonify({"message": "Hello world !"})

if __name__ == "__main__":
    app.run(debug=True)
```
`http://localhost:5000/bonjour` renvoie maintenant `{"message": "Hello world !"}`.

Dans le lien on peut ajouter des paramètres :
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/bonjour")
def index():
    nom = request.args.get("nom")
    return jsonify({"message": f"Bonjour {nom} !"})

if __name__ == "__main__":
    app.run(debug=True)
```
`http://localhost:5000/bonjour?nom=Marlon` renvoie maintenant `{"message": "Bonjour Marlon !"}`.


### Utilisation avancée

On peut utiliser Flask pour faire des sites web plus complexes. Par exemple, on peut faire un site web qui affiche une recette de cuisine :
```python
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.template_folder = "templates"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recette/:name")
def recette(name):
    return render_template(f"{name}.html")

if __name__ == "__main__":
    app.run(debug=True)
```
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mon premier site web</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Mon premier site web</h1>
    <p>Je suis un paragraphe</p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Smiley_head_happy.svg/1200px-Smiley_head_happy.svg.png" alt="Smiley">
</body>
</html>
```


# Théorie du web

## Adresses

Le web est une vaste toile sur laquelle chaque machine est reliée à d'autres machines. Pour pouvoir communiquer entre elles, les machines ont besoin d'une adresse. C'est comme une adresse postale, mais pour les machines. On appelle cela l'adresse IP (Internet Protocol). C'est une suite de chiffres qui permet d'identifier une machine sur le réseau.

Comme ce n'est pas intuitif de taper `140.82.121.3` pour aller sur github on utilise des noms de domaine. C'est une sorte de raccourci pour les adresses IP. Par exemple, `github.com` est un nom de domaine. Quand on le tape dans la barre d'adresse de notre navigateur, le navigateur va chercher l'adresse IP correspondante et va se connecter à cette adresse.

On peut le tester avec la commande `ping github.com` dans l'invite de commande. On devrait voir apparaître l'adresse IP correspondante.  
Le meilleur moyen reste d'utiliser la commande `nslookup github.com` qui permet de voir l'adresse IP et le nom de domaine correspondant. Une fois que l'on a cette adresse IP on peut essayer de regarder par où passe notre requête avec la commande `traceroute github.com`. On voit alors que le premier serveur est notre box, puis la requête passe par plusieurs serveurs avant d'arriver sur le serveur de github.


## Protocoles

Pour communiquer entre elles, les machines ont besoin de se mettre d'accord sur un protocole. C'est un ensemble de règles qui permettent de communiquer. Par exemple, pour envoyer un mail, on utilise le protocole SMTP (Simple Mail Transfer Protocol). Pour envoyer des fichiers, on utilise le protocole FTP (File Transfer Protocol). Pour afficher des pages web, on utilise le protocole HTTP (HyperText Transfer Protocol).

Depuis quelques années, on utilise de plus en plus le protocole HTTPS (HyperText Transfer Protocol Secure) qui est une version sécurisée du protocole HTTP. Il permet de chiffrer les données qui transitent sur le réseau pour éviter qu'elles soient lues par des personnes malveillantes.  
Cela assure 3 choses :
- Confidentialité : les données ne peuvent pas être lues par des personnes malveillantes
- Intégrité : les données ne peuvent pas être modifiées par des personnes malveillantes
- Authentification : on est sûr que les données proviennent bien de la bonne personne

## Codes de statut

Quand on fait une requête à un serveur, celui-ci nous renvoie un code de statut. C'est un code qui permet de savoir si la requête a fonctionné ou non. Il existe de nombreux codes de status différents. Le chiffre des centaines permet de savoir à quelle catégorie appartient le code :
- 1xx : Information
- 2xx : Succès
- 3xx : Redirection
- 4xx : Erreur client
- 5xx : Erreur serveur

Les codes les plus courants sont :
- 200 : OK (la requête a fonctionné, code le plus courant)
- 301 : Moved Permanently (la ressource demandée a été déplacée)
- 400 : Bad Request (la requête est mal formée)
- 403 : Forbidden (accès interdit)
- 404 : Not Found (la ressource demandée n'existe pas, le fameux 404)
- 500 : Internal Server Error (erreur interne du serveur, non gérée par le développeur)

Pour facilement voir les requêtes on peut utiliser la commande `curl` qui permet de faire des requêtes HTTP en ligne de commande. Par exemple, `curl -I https://www.github.com` permet de faire une requête HTTP à google. On voit alors que la requête a fonctionné et on voit le code HTML de la page d'accueil de google.


Pour illustrer les codes d'erreur vous pouvez aller sur le site [http.dog](https://http.dog/) qui permet de voir les codes d'erreur avec des images de chiens.

## Cookies

Les cookies sont des petits fichiers qui sont stockés sur la machine de l'utilisateur. Ils permettent de stocker des informations sur l'utilisateur. Par exemple, quand on se connecte à un site web, le site va stocker un cookie sur notre machine pour savoir qu'on est connecté. Cela permet de ne pas avoir à se reconnecter à chaque fois qu'on va sur le site.  
Ils sont également utilisés pour faire de la publicité ciblée. Par exemple, si on va sur un site de chaussures, on va voir des publicités pour des chaussures sur d'autres sites. C'est parce que le site de chaussures a stocké un cookie sur notre machine pour savoir qu'on est intéressé par les chaussures.  
Les cookies peuvent également être utilisés pour faire des statistiques, conserver des préférences, etc...

## Organisation d'un lien

Un lien est composé de plusieurs parties :
- le protocole : `https://`
- le nom de domaine : `www.github.com`
- le chemin : `/TristanL06/Cyrano-NSI`
- les paramètres : `?tab=repositories`
- l'ancre : `#readme`

### Le protocole

Le protocole permet de savoir comment communiquer avec le serveur. Il existe de nombreux protocoles différents, mais les plus courants sont :
- HTTP(S) : HyperText Transfer Protocol (Secure)
- FTP : File Transfer Protocol
- SMTP : Simple Mail Transfer Protocol (pour les mails)
- SSH : Secure Shell (pour se connecter à un serveur à distance)

Ils sont comme les langues, il faut que les deux machines soient d'accord sur le protocole à utiliser pour pouvoir communiquer.

### Le nom de domaine

Le nom de domaine permet de savoir à quelle machine on veut se connecter. Il est composé de plusieurs parties :
- le sous-domaine : `www`
- le domaine : `github`
- l'extension : `com`

Le sous-domaine permet de savoir à quelle partie du site on veut se connecter. Par exemple, `www` permet de se connecter à la partie publique du site, `api` permet de se connecter à l'API du site, `admin` permet de se connecter à la partie administration du site, etc...  
Le domaine permet de savoir à quelle entreprise appartient le site. Par exemple, `github` appartient à l'entreprise github.  
L'extension permet de savoir à quel type de site on veut se connecter. Par exemple, `com` est l'extension pour les sites commerciaux, `fr` est l'extension pour les sites français, `org` est l'extension pour les sites d'organisations, etc...

Tout cela est basé sur du "déclaratif", n'importe qui peut acheter presque n'importe quel nom de domaine, mais c'est en général plutôt réspecté par les entreprises.

### Le chemin

Le chemin permet de savoir quelle ressource on veut récupérer. Par exemple, `/TristanL06/Cyrano-NSI` permet de récupérer le projet Cyrano-NSI de l'utilisateur TristanL06 sur github.  
Sur une machine les fichiers sont organisés en arborescence. C'est à dire qu'il y a un dossier racine, qui contient des dossiers, qui contiennent des dossiers, etc...  
Sur un serveur web, c'est la même chose. Il y a un dossier racine qui contient des dossiers, qui contiennent des dossiers, donc pour l'arborescence suivante :
```txt
www
├── TristanL06
|   ├── Cyrano-SNT
│   |   ├── index.html
│   |   ├── style.css
│   |   └── script.js
│   └── Cyrano-NSI
│       ├── index.html
│       ├── style.css
│       └── script.js
```
On peut accéder aux fichiers `index.html` avec les liens suivants :
- `https://www.github.com/TristanL06/Cyrano-SNT/index.html`
- `https://www.github.com/TristanL06/Cyrano-NSI/index.html`

selon la ressource que l'on veut récupérer.  
En réalité certains serveurs web actuels ont un fonctionnement plus complexe, mais ça reste la norme pour la plupart des serveurs web.

### Les paramètres

Les paramètres permettent de passer des informations au serveur. Par exemple, `?tab=repositories` permet de dire au serveur qu'on veut afficher la page des dépôts d'un utilisateur sur github.

### L'ancre

L'ancre permet de se déplacer sur une page web. Par exemple, `#readme` permet de se déplacer sur la partie readme d'un projet sur github. Cela permet de faire des liens vers une partie précise d'une page web.  
Elle peut être ajouté dans le code HTML de n'importe quelle page web avec la propriété `id`. Par exemple, `<h1 id="readme">Readme</h1>` permet de créer un titre avec l'ancre `#readme`.
```html
<h1 id="readme">Readme</h1>
```

*équivalence des commandes windows/linux :*
| Windows | Linux |
| ------- | ----- |
| ping | ping |
| nslookup | nslookup |
| tracert | traceroute |
| curl | curl |
