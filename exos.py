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

        for i in range(0, self.nrb_ligne, self.sprite):
            list_ligne = []

            for j in range(0, self.nbr_colonne, self.sprite):
                list_ligne.append(ligne_count)
                ligne_count += 1
            self.mon_tableau.append(list_ligne)
            

    def find_valeur(self):

        continuer = 1
        while continuer == 1:
            
            line_number = input("Entrer un numero de ligne : ")
            column_number = input("Entrer un numero de colonne ('q' pour quitter): ")         

            if column_number == "q":
                continuer = 0
            else:
                line_number = int(line_number)
                column_number = int(column_number)
                print(self.mon_tableau[line_number][column_number])

    def find_position(self):
        
        continuer = 1
        while continuer == 1:
            valeur = input("Entrer la valeur ('q' pour quitter): ")
            
            if valeur == "q":
                continuer = 0

            else:
                valeur = int(valeur)
                recherche = 1
                while recherche == 1:
                    for ligne in self.mon_tableau:
                        if valeur in ligne:
                            l_pos = self.mon_tableau.index(ligne)
                            c_pos = self.mon_tableau[l_pos].index(valeur)
                            recherche = 0
                            print("pos = {} , {}".format(l_pos , c_pos))
                      
                    if recherche == 1:
                        print("la valeur {} n'est pas dans le tableau".format(valeur))
                        recherche = 0
                            
                
test = Tableau()
test.find_position()
