import pprint
from random import randrange, choice

"""
"""

class Labyrinth():

    """ Generate labyrinth using a file .txt
        Convert this file to a two-dimensional list
    """
    
    def __init__(self):
        self.labyrinth_txt = ""
        self.labyrinth = []
        self.open_file_txt()
        self.create_labyrinth()

    # Use file .txt for create labytinth_txt
    def open_file_txt(self):
        with open("N1.txt", "r") as labyrinth_file:
            self.labyrinth_txt = labyrinth_file.read()
    
    # Create the two-dimensional list 'labyrinth' with labyrinth_txt
    def create_labyrinth(self):
        split_laby = self.labyrinth_txt.split("\n")
        for line in split_laby:
            laby_line = []
            for caracter in line:
                laby_line.append(caracter)
            self.labyrinth.append(laby_line)

class Items():
    """ Add items at random position
    """

    def __init__(self,labyrinth):
        self.labyrinth = labyrinth
        self.random_position()
        self.create_needle()
        self.create_ether()
        self.create_syringe()
    
    # Create random position
    def random_position(self):
        lines = len(self.labyrinth)-1
        random_line = randrange(lines)
        line = self.labyrinth[random_line]
        count = 0
        column = []
        
        for caracter in line:
            if caracter == "p":
                column.append(count)
            count += 1
        random_column = choice(column)
        return (random_line, random_column)

    # Create item 'needle' at random position
    def create_needle(self):
        pos = self.random_position()
        self.labyrinth[pos[0]][pos[1]] = "N"
    
    # Create item 'ether' at random position
    def create_ether(self):
        pos = self.random_position()
        self.labyrinth[pos[0]][pos[1]] = "E"    
    
    # Create item 'syringe' at random position
    def create_syringe(self):
        pos = self.random_position()
        self.labyrinth[pos[0]][pos[1]] = "S"    

class Game():
    """ Create labyrinthe structure
    """
    def __init__(self):
        self.labyrinth = Labyrinth()
        self.items = Items(labyrinth=self.labyrinth.labyrinth)


test = Game()
pprint.pprint(test.labyrinth.labyrinth)
        
