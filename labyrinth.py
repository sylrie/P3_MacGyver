
""" Create the structure of labyrinth
"""

class Labyrinth():

    def __init__(self):

        self.labyrinth_txt = ""
        self.labyrinth = []

        self.open_file_txt()
        self.create_labyrinth()

    # Use file .txt for create labytinth_txt
    def open_file_txt(self):
        with open("resources/levels/N1.txt", "r") as labyrinth_file:
            self.labyrinth_txt = labyrinth_file.read()
    
    # Create the two-dimensional list 'labyrinth' with labyrinth_txt
    def create_labyrinth(self):
        split_laby = self.labyrinth_txt.split("\n")
        for line in split_laby:
            laby_line = []
            for Game in line:
                laby_line.append(Game)
            self.labyrinth.append(laby_line)
    

