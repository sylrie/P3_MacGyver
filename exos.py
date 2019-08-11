import pprint

class Tableau():

    def __init__(self):

        self.mon_tableau = []
        self.nrb_ligne = 15
        self.nbr_colonne = 15
        self.sprite = 1
        self.generer()

    def generer(self):

        ligne_count = 0

        for ligne in range(0, self.nrb_ligne, self.sprite):
            list_ligne = []

            for colonne in range(0, self.nbr_colonne, self.sprite):
                list_ligne.append(ligne_count)
                ligne_count += 1
            self.mon_tableau.append(list_ligne)

tableau = Tableau()
pprint.pprint(tableau.mon_tableau)