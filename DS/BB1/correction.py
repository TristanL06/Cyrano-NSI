## Correction BAC Blanc 06/12/2022

### Exercice 1

## 1
# flotte[26] renvoie {"type" : "classique", "etat" : 1, "station" : "Palais Nikaïa"}
# flotte[80]["etat"] renvoie 0
# flotte[99]["etat"] renvoie une erreur

## 2
# La variable choix peut prendre deux valeurs : "electrique" et "classique"
# Lorsque l'on choisit comme paramètre l'une des deux valeurs possibles de la variable choix cela renvoie une station où un vélo du type choisi est disponibles

## 3
for v in flotte:
    if flotte[v]["station"] == "Les Eucalyptus" and flotte[v]["etat"] == 1:
        print(v)

for v in flotte:
    if flotte[v]["type"] == "electrique" and flotte[v]["etat"] != -1:
        print(v, flotte[v]["station"])

## 4

def ping(coords):
    retour = {}
    for s in stations:
        if distance(stations[s], coords) < 800:
            retour[s] = {"nom":s, "distance":distance(stations[s], coords), "velos":[]}
    for v in flotte:
        if flotte[v]["station"] in retour.keys() and flotte[v]["etat"] == 1:
            retour[flotte[v]["station"]]["velos"] += [v]
    return retour



### Exercice 2

## 1
# il comprend nécessairement 2 déplacements vers le bas

# 3 déplacements vers la droite et 2 déplacements vers le bas font 5 déplacements
# il n'est pas possible de sauter des cases ou de revenir en arrière

## 2
# un chemin est (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3) et il vaut 16

## 3
#   4   5   6   9
#   6   6   8   10
#   9   10  15  16

## 4
# Quelle que soit la case (sauf la case (0, 0) qui vaut 4), elle vaut la somme du maximum des deux cases précédentes et de sa valeur dans T

## 5
# Le cas de base est i == 0 and j == 0 qui renvoie T[0][0]

def somme_max(T, i, j):
    if i == 0 and j == 0:
        return T[0][0]
    if i == 0 :
        return T[0][j] + somme_max(T,0,j-1)
    if j == 0 :
        return T[i][0] + somme_max(T,i-1,0)
    return T[i][j] + max(somme_max(T,i-1,j), somme_max(T,i,j-1))

somme_max(T,2,3)


### Exercice 3
def donnePremierIndiceLibre(Mousse):
    i = 0
    while i <= len(Mousse) and Mousse[i] != None :
        i += 1
    return i

def PlaceBulle(b):
    i = donnePremierIndiceLibre(Mousse)
    if i < len(Mousse):
        Mousse[i] = b

def bullesEnContact(B1, B2):
    return distanceEntreBulles(B1, B2) <= B1.rayon + B2.rayon:

def collision(indPetite, indGrosse, mousse):
    # calcul du nouveau rayon de la grosse bulle
    surfPetite = pi*Mousse[indPetite].rayon**2
    surfGrosse = pi*Mousse[indGrosse].rayon**2
    surfGrosseApresCollision = surfPetite + surfGrosse
    rayonGrosseApresCollision = sqrt(surfGrosseApresCollision/pi) 
    #réduction de 50% de la vitesse de la grosse bulle
    Mousse[indGrosse].dirx = Mousse[indGrosse].dirx/2
    Mousse[indGrosse].diry = Mousse[indGrosse].diry/2
    #suppression de la petite bulle dans Mousse
    Mousse[indPetite] = None
