# Les fonctions et procédures


## Fonction

Pour rendre le code plus lisible et éviter les répétitions on peut définir des fonctions.
Les fonctions ont toujours la même structure :
```python
def nom(paramètre1, paramètre2 ...):
	#calcul
	return variable_de_retour
```
elles prennent en **argument** des **paramètres** et **retournent** un résultat.

Nous pouvons par exemple définir une fonction qui fait la somme entre deux nombre entiers :
```python
def somme(a, b): #fait la somme entre a et b et le retourne
	c = a + b
	return c
```
On peut donc **appeler** la fonction :

```python
nombre_a = 8
nombre_b = 10

nombre_c = somme(nombre_a, nombre_b)
print(nombre_c)
```

On peut également utiliser les fonctions pour éviter des répétitions dans un code. Par exemple le code suivant donne une appréciation en fonction de la note, à chaque élève, et à la classe au global :
```python
notes = [5, 12, 6, 18, 20, 20, 15, 14] #notes des élèves

appréciations = []
for n in notes:
	appréciation = ""
	if n < 7:
		appréciation = "Insuffisant"
	elif n < 10:
		appréciation = "Presque la moyenne"
	elif n < 16:
		appréciation = "Bien joué"
	else:
		appréciation = "Excellent !"
	appréciations.append(appréciation)

moyenne = sum(notes) / len(notes) #la moyenne est la somme sur le nombre de notes
if moyenne < 7:
	appréciation = "Insuffisant"
elif moyenne < 10:
	appréciation = "Presque la moyenne"
elif moyenne < 16:
	appréciation = "Bien joué"
else:
	appréciation = "Excellent !"

print(appréciations) # appréciations de chaque élève
print(appréciation) # appréciation de la classe
```
De manière évidente les conditions permettant de choisir l'appréciation sont écrites deux fois dans le code. On peut donc les mettre dans une fonction prenant en paramètre la note et renvoyer l'appréciation associée :
```python
def appréciation(note):
	if n < 7:
		a = "Insuffisant"
	elif n < 10:
		a = "Presque la moyenne"
	elif note < 16:
		a = "Bien joué"
	else:
		a = "Excellent !"
	return a
```

Et on peut réécrire tout le code avec cette nouvelle fonction :
```python
def appréciation(note):
	if note < 7:
		a = "Insuffisant"
	elif note < 10:
		a = "Presque la moyenne"
	elif note < 16:
		a = "Bien joué"
	else:
		a = "Excellent !"
	return a

notes = [5, 12, 6, 18, 20, 20, 15, 14] #notes des élèves

appréciations = []
for n in notes:
	appr = appréciation(n)
	appréciations.append(appr)

moyenne = sum(notes) / len(notes) #la moyenne est la somme sur le nombre de notes
appr = appréciation(moyenne)

print(appréciations) # appréciations de chaque élève
print(appr) # appréciation de la classe
```

## Return
le mot-clé `return` permet de retourner une valeur. Il est lié à une fonction.+

> ⚠ Il est absolument **interdit** d'utiliser return en dehors d'une fonction !!!

Une return arrête l'exécution d'une fonction.
On peut donc réécrire légèrement la fonction appréciation :
```python
def appréciation(note):
	if n < 7:
		return "Insuffisant"
	elif n < 10:
		return "Presque la moyenne"
	elif note < 16:
		return "Bien joué"
	return "Excellent !"
```

On a pu enlever le `else` car si on arrive à cette étape de l'exécution on n'est dans aucun des cas présents au-dessus.
On peut également remplacer tous les `elif` par des `if` simples pour la même raison :
```python
def appréciation(note):
	if n < 7:
		return "Insuffisant"
	if n < 10:
		return "Presque la moyenne"
	if note < 16:
		return "Bien joué"
	return "Excellent !"
```

## Procédure

Une procédure est une fonction qui ne retourne rien. On peut l'utiliser pour écrire dans un fichier, modifier une liste, exécuter une action...
De manière globale, les fonctions et procédures sont regroupés sous l'appellation "fonction" mais il faut garder cette différence en tête.
