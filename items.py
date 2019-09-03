""" items
    Create random positions for items and place them on the labyrinth
"""
# library imports
from random import randrange, choice

class Items():
    """ Create random positions for items and place them on the labyrinth
    """
    
    def __init__(self, labyrinth):
       
        self.labyrinth = labyrinth
        self.create_items()
   
    def random_position(self, item):
        """ Create random positions for items
        """

        item = item
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
        self.labyrinth[random_line][random_column] = item

    def create_items(self):
        """ create items
        """
        
        self.items_list = ("Dropper", "Syringe", "Tube", "Heart")
        
        self.items_dict = {}

        for item in self.items_list:
            self.items_dict[item[0]] = item # ex: {'D': 'Dropper'}
            self.random_position(item[0]) # ex :use random position for 'D'




