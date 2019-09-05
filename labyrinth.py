
""" labyrinth
    Create the structure of full labyrinth
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

# library import
from random import randrange, choice

class Labyrinth():
    """ Create the structure of full labyrinth with a file level.txt
        add items at random position on the labyrinth
    """

    def __init__(self, level):

        self.level = level
        self.labyrinth_txt = ""
        self.labyrinth = []

        self.open_file_txt()
        self.create_labyrinth()
        self.create_items()

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
            for game in line:
                laby_line.append(game)
            self.labyrinth.append(laby_line)

    def random_position(self, item):
        """ Chose a random positions for item
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

        self.items_list = ("Armor", "Helmet", "Dagger", "Life")
        for item in self.items_list:

            self.random_position(item[0])
