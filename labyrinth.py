
""" Create the structure of full labyrinth
"""
import items

class Labyrinth():
    """ Create the structure of full labyrinth 
    """

    def __init__(self):

        self.labyrinth_txt = ""
        self.labyrinth = []

        self.open_file_txt()
        self.create_labyrinth()
        self.add_items()

    # Use file .txt for create labytinth_txt
    def open_file_txt(self):
        with open("resources/levels/N2.txt", "r") as labyrinth_file:
            self.labyrinth_txt = labyrinth_file.read()
    
    # Create the two-dimensional list 'labyrinth' with labyrinth_txt
    def create_labyrinth(self):
        split_laby = self.labyrinth_txt.split("\n")
        for line in split_laby:
            laby_line = []
            for Game in line:
                laby_line.append(Game)
            self.labyrinth.append(laby_line)
    
    # Add items with Class Items()
    def add_items(self):
        self.items = items.Items(self.labyrinth)
