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

## Exercice 4 : Fichiers CSV
Dans cet exercice on va travailler avec des fichiers CSV. On va utiliser un fichier qui contient des informations sur des élèves de Poudlard. Ce fichier est disponible sur github (élèves.csv).

1) Écrire une fonction qui prend en argument le nom d'un fichier CSV et qui renvoie une liste de tous les élèves présents dans le fichier.
2) Écrire une fonction qui prend en argument une liste de notes et qui renvoie la moyenne de ces notes.
3) Écrire une fonction qui prend en argument le nom d'un fichier CSV et qui renvoie la moyenne de chaque élève.
4) Afficher chaque élève et sa moyenne dans le terminal.

## Exercice 5 : Écrire un fichier CSV
Dans cet exercice on va simuler un lancer de dés et enregistrer les résultats dans un fichier CSV. On rappelle que le lancer d'un dé à 6 faces est un tirage aléatoire d'un nombre entier entre 1 et 6, on peut utiliser la fonction `randint` du module `random` pour simuler ce lancer.

1) Générer 10 lancers de 5 dés en affichant les résultats dans le terminal (chaque dés et la somme des dés).
2) Faire de même mais en enregistrant les résultats dans un fichier CSV. On pourra utiliser la fonction `write()` pour écrire dans le fichier.
3) Transformer le code précédent en une fonction qui prend en argument le nombre de dés et le nombre de lancers et qui enregistre les résultats dans un fichier CSV.

## Exercice 6 : Exploiter un fichier CSV
On travaille maintenant sur le fichier météo.csv disponible sur github. Ce fichier contient des données météo captées à Sophia.

1) Écrire une fonction qui prend en argument une échéance et qui renvoie la température à cette échéance.
2) Écrire un code qui calcule la moyenne de toutes les données et qui l'affiche dans le terminal sous forme `nom : moyenne`.
3) Reprendre le code précédent et engegistrer les résultats dans un fichier CSV.
