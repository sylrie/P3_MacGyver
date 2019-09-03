
""" labyrinth
    Create the structure of full labyrinth
"""

# programs import
import items

class Labyrinth():
    """ Create the structure of full labyrinth 
    """

    def __init__(self, level):

        self.level = level
        self.labyrinth_txt = ""
        self.labyrinth = []

        self.open_file_txt()
        self.create_labyrinth()
        self.add_items()

    
    def open_file_txt(self):
        """ Use file .txt for create labytinth_txt
        """

        with open("resources/levels/"+self.level+".txt", "r") as labyrinth_file:
            self.labyrinth_txt = labyrinth_file.read()
       
    def create_labyrinth(self):
        """ Create the two-dimensional list 'labyrinth' with labyrinth_txt
        """
        split_laby = self.labyrinth_txt.split("\n")
        for line in split_laby:
            laby_line = []
            for Game in line:
                laby_line.append(Game)
            self.labyrinth.append(laby_line)
    
    
    def add_items(self):
        """ Add items with Class Items()
        """
        
        self.items = items.Items(self.labyrinth)
