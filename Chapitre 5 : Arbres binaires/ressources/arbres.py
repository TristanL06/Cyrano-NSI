class arbreBinaire:
    def __init__(self, arbre):
        self.droit = None
        self.gauche = None
        if type(arbre) == str:
            self.étiquette = arbre
            return
        self.étiquette = arbre[0]
        if arbre[1] != None:
            self.gauche = arbreBinaire(arbre[1])
        if arbre[2] != None:
            self.droit = arbreBinaire(arbre[2])

    def taille(self):
        taille = 1
        if self.droit != None:
            taille += self.droit.taille()
        if self.gauche != None:
            taille += self.gauche.taille()
        return taille

    def profondeur(self):
        profondeur = 0
        if self.droit != None:
            profondeur = self.droit.profondeur() + 1
        if self.gauche != None:
            profondeur = max(profondeur, self.gauche.profondeur() + 1)
        return profondeur

    def prefixe(self):
        print(self.étiquette)
        if self.gauche != None:
            self.gauche.prefixe()
        if self.droit != None:
            self.droit.prefixe()

    def infixe(self):
        if self.gauche != None:
            self.gauche.infixe()
        print(self.étiquette)
        if self.droit != None:
            self.droit.infixe()

    def suffixe(self):
        if self.gauche != None:
            self.gauche.suffixe()
        if self.droit != None:
            self.droit.suffixe()
        print(self.étiquette)

""" Création des arbres de l'exercice 1 depuis les tuples
arbres = []
arbres.append(
    (
        'T',
        (
            'Y',
            'P',
            None
            ),
        (
            'O',
            (
                'H',
                None,
                None
                ),
            (
                'N',
                None,
                None)
            )
        )
    )

arbres.append(
    (
        'N',
        (
            'Y',
            (
                'D',
                'C',
                'O'
                ),
            (
                'P',
                'E',
                None
                )
            ),
        (
            'O',
            'T',
            'H'
            )
        )
    )

arbres.append(
    (
        "x",
        (
            "+",
            "4",
            "2"
            ),
        (
            "-",
            "9",
            (
                "+",
                "1",
                "1"
                )
            )
        )
    )

arbres.append(
    (
        '10',
        (
            '8',
            (
                '5',
                '4',
                '2'
                ),
            (
                '6',
                '3',
                None
                )
            ),
        (
            '4',
            '2',
            '1'
            )
        )
    )
"""
