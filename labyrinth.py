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
            for Game in line:
                laby_line.append(Game)
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
        
        for Game in line:
            if Game == "p":
                column.append(count)
            count += 1
        random_column = choice(column)
        return (random_line, random_column)

    # Create item 'needle' at random position
    def create_needle(self):
        init_position = self.random_position()
        self.labyrinth[init_position[0]][init_position[1]] = "N"
    
    # Create item 'ether' at random position
    def create_ether(self):
        init_position = self.random_position()
        self.labyrinth[init_position[0]][init_position[1]] = "E"    
    
    # Create item 'syringe' at random position
    def create_syringe(self):
        init_position = self.random_position()
        self.labyrinth[init_position[0]][init_position[1]] = "S"    

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
        self.Get_init_position()
        self.player_movement()
       
    # Find player initial position
    def Get_init_position (self):
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

    def player_movement(self):
        movement_request = ""
        line_pos = self.line_pos
        column_pos = self.column_pos
        self.count_item = 3
        run = 1
        
        while run == 1:
            pprint.pprint(self.labyrinth)
            movement_request = input("Choose a way (q for QUIT)(r for RIGHT, l for LEFT, u for UP, d for DOWN) : ")

            if movement_request == "q":
                run = 0

            #Define the request position and check if new position is still in labyrinth
            if movement_request == "r" and column_pos <= 14:
                column_pos += 1
                sprite_content = self.labyrinth[line_pos][column_pos]  
            elif movement_request == "l" and column_pos >= 1:
                column_pos -= 1
                sprite_content = self.labyrinth[line_pos][column_pos]
            elif movement_request == "d" and line_pos <= 14:
                line_pos += 1
                sprite_content = self.labyrinth[line_pos][column_pos]
            elif movement_request == "u" and line_pos >= 1:
                line_pos -= 1
                sprite_content = self.labyrinth[line_pos][column_pos]
            
            # if sprite is not a wall, change actual position into passage 'p' and change new player position 'X'
            if sprite_content != "w":
                self.labyrinth[self.line_pos][self.column_pos] = "p"
                self.line_pos = line_pos
                self.column_pos = column_pos
                self.labyrinth[self.line_pos][self.column_pos] = "X"
            
            # if player is on an item posisition, change count of remaining item    
            if sprite_content == "N" or sprite_content == "E" or sprite_content == "S":
                self.count_item -= 1
                print("you picked one item")
            
            # ifplayer is at the labyrinth's exit, check if it's a win,... or not
            if sprite_content == "a" and self.count_item == 0:
                print("!! YOU WIN !!")
                run = 0
            if sprite_content == "a" and self.count_item > 0:
                print("!!YOU LOOOOOSE !!")
                run = 0
            # if sprite is a wall, cancel movement
            else:
                line_pos = self.line_pos
                column_pos = self.column_pos
            

test = Game()
            