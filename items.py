
""" Create random positions for items and place them on the labyrinth
    """

from random import randrange, choice
from labyrinth import *

class Items():
    
    def __init__(self):
        labyrinth = Labyrinth()
        self.labyrinth = labyrinth.labyrinth 
             
        self.tube_position = ()
        self.syringe_position = ()
        self.dropper_position = ()
        self.heart_position = ()

        self.items_position()

    def random_position(self):
        lines = len(self.labyrinth)-1
        random_line = randrange(lines)
        line = self.labyrinth[random_line]
        count = 0
        column = []
        
        for sprite in line:
            if sprite == "p":
                column.append(count)
            count += 1
        random_column = choice(column)
        return (random_line, random_column)

    def items_position(self):
        
        # create Tube
        self.tube_position = self.random_position()
        self.labyrinth[self.tube_position[0]][self.tube_position[1]] = "T"
        # Create Syringe
        self.syringe_position = self.random_position()
        self.labyrinth[self.syringe_position[0]][self.syringe_position[1]] = "S"
        # Create Dropper
        self.dropper_position =self.random_position()
        self.labyrinth[self.dropper_position[0]][self.dropper_position[1]] = "D"
        # Create Heart
        self.heart_position =self.random_position()
        self.labyrinth[self.heart_position[0]][self.heart_position[1]] = "H"


