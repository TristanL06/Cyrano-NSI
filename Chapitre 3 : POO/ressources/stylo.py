class Stylo:
    def __init__(self, max_taille):
        self.cartouche = None
        self.max_taille = max_taille

    def changeCartouche(self, cartouche):
        if cartouche.taille > self.max_taille:
            raise TypeError("cartouche trop grosse")
        self.cartouche = cartouche

    def affiche_qte(self):
        print(self.cartouche.quantite)

    def utilise(self, distance):
        self.cartouche.use(distance)

    def getCouleur(self):
        return self.cartouche.couleur

    def estVide(self):
        return self.cartouche.estVide()

class Cartouche:
    def __init__(self, couleur, quantite, taille):
        self.couleur = couleur
        self.quantite = quantite
        self.taille = taille

    def use(self, quantite):        
        if self.quantite < quantite:
            raise TypeError("pas assez d'encre")
        self.quantite -= quantite

    def estVide(self):
        return self.quantite == 0
        
cartouche = Cartouche("rouge", 2500, 15)
cartouche3 = Cartouche("vert", 1200, 15)
cartouche2 = Cartouche("bleue", 2500, 25)
stylo = Stylo(15)
stylo.changeCartouche(cartouche)
print(stylo.estVide())
stylo.affiche_qte()
stylo.utilise(2500)
print(stylo.estVide())
stylo.affiche_qte()
stylo.changeCartouche(cartouche3)
print(stylo.estVide())
stylo.affiche_qte()
