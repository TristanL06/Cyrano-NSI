## Exercice 1 : Lire un fichier

1) Écrire un programme qui lit un fichier texte et affiche son contenu grâce à la fonction `read()`
2) Écrire un programme qui lit un fichier texte et affiche son contenu grâce à la fonction `readlines()`. Quelle est la différence avec la fonction `read()` ?

## Exercice 2 : Écrire dans un fichier

1) Écrire un programme qui écrit dans un fichier texte grâce à la fonction `write()`
2) Écrire une fonction qui prend en argument une liste de mots sours forme de strings et qui écrit chacune de ces chaînes dans un fichier texte en utilisant la fonction `write()`. Comment faire pour que chaque mot soit écrit sur une ligne différente ?
3) Quel autre mode peut être utilisé pour faire ça ? Écrire la fonction correspondante.

## Exercice 3 : Analyser des données
Dans cet exercice on va analyser trois fichiers. Chaque fichier contient le même texte, mais dans 3 langues différentes : français, anglais et espagnol. C'est fichiers txt sont disponibles sur github.

1) Écrire une fonction qui prend en argument le nom d'un fichier et qui renvoie une liste de tous les caractères (différents) présents dans le fichier.
2) Écrire une fonction qui prend en argument le nom d'un fichier et qui renvoie le nombre de chaque caractère présent dans le fichier (il pourra être renvoyé sous forme d'un dictionnaire).
3) Écrire un programme utilisant la fonction précédente pour faire un classement des caractères les plus utilisés dans chaque fichier. Que remarque-t-on ?
4) Modifier la fonction de la question 2 pour qu'elle renvoie le nombre de chaque caractère présent dans le fichier, mais en ignorant les signes de ponctuation, les espaces et les retours à la ligne.
