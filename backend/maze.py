
""" maze
    Create the full structure of the maze 
    w = wall    p = path    f = golem

    add items at random position on the maze
    A = Armor   H = Helmet  S = Sword   L = Life
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

# library import
from random import randrange, choice

class Maze():
    """ Create the structure of full maze with a file.txt
        
    """

    def __init__(self):

        self.maze_txt = ""
        self.maze = []

        self.open_file_txt()
        self.create_labyrinth()
        self.create_items()

    def open_file_txt(self):
        """ Use file .txt for create maze_txt
        """

        with open("resources/levels/level1.txt", "r") as level_file:
            self.maze_txt = level_file.read()

    def create_labyrinth(self):
        """ Create the two-dimensional list 'maze' with maze_txt
        """
        split_laby = self.maze_txt.split("\n")
        for line in split_laby:
            laby_line = []
            for game in line:
                laby_line.append(game)
            self.maze.append(laby_line)

    def random_position(self, item):
        """ Chose a random positions for item
        """

        item = item
        lines = len(self.maze)-1
        random_line = randrange(lines)
        line = self.maze[random_line]
        count = 0
        column = []

        while column == []:
            for sprite in line:
                if sprite == "p":
                    column.append(count)

                count += 1

        random_column = choice(column)
        self.maze[random_line][random_column] = item

    def create_items(self):
        """ create items
        """

        self.items_list = ("Armor", "Helmet", "Sword", "Life")
        for item in self.items_list:

            self.random_position(item[0])
