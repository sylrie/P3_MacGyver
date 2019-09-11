
""" maze display
    display maze interface
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

# pylint: disable=no-member

# library import
import pygame

# programs import
from backend.maze import Maze
from backend.player import Player

class MazeDisplay():
    """ Display maze interface
    """

    def __init__(self):

        self.sprite_cote = 40
        self.active_interface = "game"
        self.player_pic = None

        self.init_game()
        self.create_surface()
        self.load_images()
        self.create_rect()
        self.display()

    def init_game(self):
        """ Generate maze and load player values
        """

        self.lab = Maze()
        self.maze = self.lab.maze

        self.player = Player(self.maze)
        self.maze = self.player.maze
        self.game_status = self.player.game_status

    def create_surface(self):
        """ Create pygame surface
        """

        pygame.init()

        icone = pygame.image.load("resources/images/icon.png")
        pygame.display.set_icon(icone)

        pygame.display.set_caption("MacGyver - Maze - Level 1")

        self.window_surface = pygame.display.set_mode((600, 680))

    def load_images(self):
        """ load resources
        """

        ### Player ###
        player = "resources/images/player/"

        self.playerdown = pygame.image.load(
            player + "playerdown.png"
        ).convert_alpha()

        self.playerup = pygame.image.load(
            player + "playerup.png"
        ).convert_alpha()

        self.playerright = pygame.image.load(
            player + "playerright.png"
        ).convert_alpha()

        self.playerleft = pygame.image.load(
            player + "playerleft.png"
        ).convert_alpha()

        ### Inventory ###
        inventory = "resources/images/inventory/"

        self.inventory_pic = pygame.image.load(
            inventory + "inventory.png"
        ).convert()

        self.armor = pygame.image.load(
            inventory + "armor.png"
        ).convert_alpha()

        self.armor_menu = pygame.image.load(
            inventory + "armor2.png"
        ).convert_alpha()

        self.helmet = pygame.image.load(
            inventory + "helmet.png"
        ).convert_alpha()

        self.helmet_menu = pygame.image.load(
            inventory + "helmet2.png"
        ).convert_alpha()

        self.dagger = pygame.image.load(
            inventory + "dagger.png"
        ).convert_alpha()

        self.dagger_menu = pygame.image.load(
            inventory + "dagger2.png"
        ).convert_alpha()

        ### life images ###
        self.life = pygame.image.load(
            inventory + "life.png"
        ).convert_alpha()

        self.life1 = pygame.image.load(
            inventory + "life1.png"
        ).convert_alpha()

        self.life2 = pygame.image.load(
            inventory + "life2.png"
        ).convert_alpha()
        self.life3 = pygame.image.load(
            inventory + "life3.png"
        ).convert_alpha()

        ### maze ###
        maze = "resources/images/maze/"
        # Wall
        self.wall = pygame.image.load(
            maze + "wall.png"
        ).convert()

        # Passage
        self.path_pic = pygame.image.load(
            maze + "wood.png"
        ).convert()
        # Gardian
        self.gardian = pygame.image.load(
            maze + "gardian.png"
        ).convert_alpha()
        # fire
        self.golem_pic = pygame.image.load(
            maze + "golem.png"
        ).convert_alpha()
        # buttons
        self.restart_button = pygame.image.load(
            maze + "B_restart.png"
        ).convert()
        self.home_button = pygame.image.load(
            maze + "B_home.png"
        ).convert()

    def create_rect(self):
        """ Create rect
        """

        self.restart_rect = pygame.Rect((0, 610), (100, 30))
        self.quit_game_rect = pygame.Rect((0, 645), (100, 30))

    def display_maze(self):
        """ display maze images
        """

        line_nbr = 0
        for line in self.maze:
            column_nbr = 0
            for sprite in line:

                column = column_nbr * self.sprite_cote
                line = line_nbr * self.sprite_cote

                if sprite != "w":
                    self.window_surface.blit(self.path_pic, [column, line])

                if sprite == 'w':
                    self.window_surface.blit(self.wall, [column, line])
                elif sprite == "f":
                    self.window_surface.blit(self.golem_pic, [column, line])
                elif sprite == "a":
                    self.window_surface.blit(self.gardian, [column, line])
                elif sprite == 'A':
                    self.window_surface.blit(self.armor, [column, line])
                elif sprite == 'H':
                    self.window_surface.blit(self.helmet, [column, line])
                elif sprite == 'S':
                    self.window_surface.blit(self.dagger, [column, line])
                elif sprite == "L":
                    self.window_surface.blit(self.life, [column, line])
                else:
                    pass
                column_nbr += 1

            line_nbr += 1

    def display_menu(self):
        """ display menu image
        """

        self.window_surface.blit(self.restart_button, (0, 605))
        self.window_surface.blit(self.home_button, (0, 638))

        # Display life
        if self.player.health == 0:
            self.window_surface.blit(self.life1, (440, 615))
        elif self.player.health == 1:
            self.window_surface.blit(self.life2, (440, 615))
        elif self.player.health == 2:
            self.window_surface.blit(self.life3, (440, 615))

        # Display inventory
        self.window_surface.blit(self.inventory_pic, (155, 610))
        if "A" in self.player.inventory:
            self.window_surface.blit(self.armor, (8*self.sprite_cote, 620))
        else:
            self.window_surface.blit(self.armor_menu, (8*self.sprite_cote, 620))
        if "H" in self.player.inventory:
            self.window_surface.blit(self.helmet, (6*self.sprite_cote, 620))
        else:
            self.window_surface.blit(self.helmet_menu, (6*self.sprite_cote, 620))
        if "S" in self.player.inventory:
            self.window_surface.blit(self.dagger, (4*self.sprite_cote, 620))
        else:
            self.window_surface.blit(self.dagger_menu, (4*self.sprite_cote, 620))

    def pygame_event(self):
        """ Manage all pygame event
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.restart_rect.collidepoint(event.pos):
                        self.init_game()

                    if self.quit_game_rect.collidepoint(event.pos):
                        self.player.game_status = "home"

            # request movement using method movement_request() from Class Player()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    self.player.movement_request("RIGHT")
                    self.player_pic = self.playerright

                if event.key == pygame.K_LEFT:
                    self.player.movement_request("LEFT")
                    self.player_pic = self.playerleft

                if event.key == pygame.K_DOWN:
                    self.player.movement_request("DOWN")
                    self.player_pic = self.playerdown

                if event.key == pygame.K_UP:
                    self.player.movement_request("UP")
                    self.player_pic = self.playerup

    def display(self):
        """ Dispaly maze surface
        """
        # initial player pic
        self.player_pic = self.playerdown

        # set repeat mode for keydown
        pygame.key.set_repeat(100, 70)

        # display loop
        while self.player.game_status == "game":

            # Display menu
            self.display_menu()

            # Display maze
            self.display_maze()

            # player position in pixel
            self.player_position = (
                self.player.player_position[0] * self.sprite_cote, \
                self.player.player_position[1] * self.sprite_cote)

            # display player
            self.window_surface.blit(self.player_pic, self.player_position)

            # chack for Pygame event
            self.pygame_event()

            # refresh interface
            self.interface = self.player.game_status

            # Refresh pygame display
            pygame.display.flip()
