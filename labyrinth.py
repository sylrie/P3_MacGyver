import pprint
from random import randrange, choice

""" Create the structure of the labyrinth using the N1.txt file
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
            for Game in line:
                laby_line.append(Game)
            self.labyrinth.append(laby_line)

class Items():
    """ Add items at random position
    """

    def __init__(self,labyrinth):
        self.labyrinth = labyrinth
        self.random_position()
        self.create_tube()
        self.create_dropper()
        self.create_syringe()
        self.create_heart()
    
    # Create random position
    def random_position(self):
        lines = len(self.labyrinth)-1
        random_line = randrange(lines)
        line = self.labyrinth[random_line]
        count = 0
        column = []
        
        for Game in line:
            if Game == "p":
                column.append(count)
            count += 1
        random_column = choice(column)
        return (random_line, random_column)

    # Create item 'tube' at random position
    def create_tube(self):
        init_position = self.random_position()
        self.labyrinth[init_position[0]][init_position[1]] = "T"
    
    # Create item 'dropper' at random position
    def create_dropper(self):
        init_position = self.random_position()
        self.labyrinth[init_position[0]][init_position[1]] = "D"    
    
    # Create item 'syringe' at random position
    def create_syringe(self):
        init_position = self.random_position()
        self.labyrinth[init_position[0]][init_position[1]] = "S" 

    # Create item 'heart' at random position
    def create_heart(self):
        init_position = self.random_position()
        self.labyrinth[init_position[0]][init_position[1]] = "H"   

class Create_game():
    """ Create labyrinthe structure
    """
    def __init__(self):
        self.labyrinth = Labyrinth()
        self.items = Items(labyrinth=self.labyrinth.labyrinth)

class Game():

    def __init__(self):
        labyrinth = Create_game()
        self.labyrinth =labyrinth.labyrinth.labyrinth
        self.get_init_position()
             
    # Find player initial position 'd'
    def get_init_position (self):
        self.init_position = ()
        self.line_pos = 0
        self.column_pos = 0
        position = "d"
        count_line = 0
        search = 1
        while search == 1:
            
            for line in self.labyrinth:

                if position in line:
                    self.line_pos = count_line
                    column_pos = self.labyrinth[self.line_pos].index(position)
                    search = 0
                    self.init_position = (self.line_pos, self.column_pos)
                    self.labyrinth[self.line_pos][self.column_pos] = "X"
                count_line += 1
 
            