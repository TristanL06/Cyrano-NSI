## Correction DS1 NSI 09/11/2022

print("\n===== EXERCICE 1 =====")

tab = [30.5, 15.0, 6.0, 20.0, 5.0, 35.0, 10.5]
#tab=[30.5, 15.0, 20.0, 6.0, 5.0, 35.0, 10.5]
print("\n=== Question 1. (a)===")

def total_hors_reduction (tab):
    somme = 0
    for article in tab:
        somme += article
    return somme

print(total_hors_reduction(tab))

print("\n=== Question 1. (b)===")

def offre_bienvenue(tab):
    """ tableau -> float """
    somme = 0
    longueur = len(tab)
    if longueur > 0:
    	somme = tab[0] * 0.8
    if longueur > 1:
        somme = somme + tab[1] * 0.7
    if longueur > 2:
        for i in range(2, longueur):
            somme = somme + tab[i]
    return somme

print(offre_bienvenue(tab))

print("\n=== Question 2 ===")

def prix_solde(tab):
    taille = len(tab)
    if taille == 1:
        return total_hors_reduction(tab) * 0.9
    elif taille == 2:
        return total_hors_reduction(tab) * 0.8
    elif taille == 3:
        return total_hors_reduction(tab) * 0.7
    elif taille == 4:
        return total_hors_reduction(tab) * 0.6
    else:
        return total_hors_reduction(tab) * 0.5

print(prix_solde(tab))

print("\n=== Question 3. (a) ===")

def minimum(tab):
    mini = tab[0]
    for i in range(1,len(tab)):
        if tab[i] < mini:
            mini = tab[i]
    return mini

print(minimum(tab))

print("\n=== Question 3. (b) ===")

def offre_bon_client(tab):
    prix = total_hors_reduction(tab)
    if len(tab) >= 2:
        prix -= minimum(tab)
    return prix

print(offre_bon_client(tab))

print("\n=== Question 4 (a) ===")
print("On peut prendre le panier [30.5, 5.0, 6.0, 20.0, 15.0, 35.0, 10.5].")
print("\n=== Question 4 (b) ===")
print("Le panier le moins cher est : [35.0, 30.5, 20.0, 15.0, 10.5, 6.0, 5.0], qui vaut 96€.")
print("\n=== Question 4 (c) ===")
print("Le client peut utiliser un algorithme de tri pour trier la liste de façon décroissante.")


print("\n\n===== EXERCICE 2 =====")

print("\n=== Question 1 ===")

def syracuse(n):
    termes = [n]
    while n > 1:
        if n%2 == 0:
            n = n//2
        else:
            n = n * 3 + 1
        termes.append(n)
    return termes

print(syracuse(14))


print("\n=== Question 2 ===")

def syracuse_recursif(n, termes):
    termes.append(n)
    if n == 1:
        return termes
    if n%2 == 0:
        return syracuse_recursif(n//2,termes)
    return syracuse_recursif(n*3+1,termes)

print(syracuse_recursif(14, []))

print("\n=== Question 3 ===")

def syracuse_TDV(n, tempsDeVol = 0):
    if n == 1:
        return tempsDeVol
    if n%2 == 0:
        return syracuse_TDV(n//2,tempsDeVol + 1)
    return syracuse_TDV(n*3+1,tempsDeVol + 1)

print(syracuse_TDV(14))


print("\n=== Question 4 ===")

def syracuse_AM(n, maxi = 0):
    if maxi < n:
        maxi = n
    if n == 1:
        return maxi
    if n%2 == 0:
        return syracuse_AM(n//2,maxi)
    return syracuse_AM(n*3+1,maxi)

print(syracuse_AM(14))


print("\n=== Question 5 ===")

def syracuse_TDVA(n, N = None, tempsAltitude = 0):
    if N == None:
        N = n
    if n < N:
        return tempsAltitude - 1
    if n%2 == 0:
        return syracuse_TDVA(n//2, N, tempsAltitude + 1)
    return syracuse_TDVA(n*3+1, N, tempsAltitude + 1)

print(syracuse_TDVA(5))
