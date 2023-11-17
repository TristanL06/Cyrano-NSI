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
    <link rel="stylesheet" href="style.css"> /* On ajoute cette ligne */
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
    <script src="script.js"></script> /* On ajoute cette ligne */
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
