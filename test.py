
liste1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
liste2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
value = 19
liste = [liste1,liste2]
ligne = len(liste)
continuer = 1


for line in range(ligne):

    if value in line:
        l = liste.index(line)
        c = liste[l].index(value)
            
print("pos = {} , {}".format(l , c))
            
            
        
   