
""" game display
    display game interface
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

# pylint: disable=no-member

# library import
import pygame

# programs import
from backend.labyrinth import GenerateLabyrinth
from backend.player import Player

class LabyDisplay():
    """ Display laby interface
    """

    def __init__(self):

        self.sprite_cote = 40
        self.active_interface = "game"

        self.player_pic = None
        self.init_game()
        self.create_surface()
        self.loads()
        self.create_rect()
        self.display()

    def init_game(self):
        """ Generate labyrinth and load player values
        """

        self.lab = GenerateLabyrinth()
        self.labyrinth = self.lab.labyrinth

        self.player = Player(self.labyrinth)
        self.labyrinth = self.player.labyrinth
        self.run = self.player.run

    def create_surface(self):
        """ Create pygame surface
        """

        pygame.init()
        pygame.display.set_caption("MacGyver Labyrinth")
        self.window_surface = pygame.display.set_mode((600, 680))

    def loads(self):
        """ load resources
        """

        # Player
        self.playerdown = pygame.image.load("resources/images/playerdown.png").convert_alpha()
        self.playerup = pygame.image.load("resources/images/playerup.png").convert_alpha()
        self.playerright = pygame.image.load("resources/images/playerright.png").convert_alpha()
        self.playerleft = pygame.image.load("resources/images/playerleft.png").convert_alpha()

        # Gardian
        self.gardian = pygame.image.load("resources/images/gardian.png").convert_alpha()
        # Wall
        self.wall_pic = pygame.image.load("resources/images/wall.png").convert()
        # Passage
        self.path_pic = pygame.image.load("resources/images/grass2.png").convert()
        # water
        self.water_pic = pygame.image.load("resources/images/background.png").convert()

        # Inventory
        self.inventory_pic = pygame.image.load("resources/images/inventory2.png")

        self.armor = pygame.image.load("resources/images/armor.png").convert_alpha()
        self.armor_menu = pygame.image.load("resources/images/armor2.png").convert_alpha()

        self.helmet = pygame.image.load("resources/images/helmet.png").convert_alpha()
        self.helmet_menu = pygame.image.load("resources/images/helmet2.png").convert_alpha()

        self.dagger = pygame.image.load("resources/images/dagger.png").convert_alpha()
        self.dagger_menu = pygame.image.load("resources/images/dagger2.png").convert_alpha()

        # life images
        self.life = pygame.image.load("resources/images/life.png").convert_alpha()
        self.life1 = pygame.image.load("resources/images/life1.png").convert_alpha()
        self.life2 = pygame.image.load("resources/images/life2.png").convert_alpha()
        self.life3 = pygame.image.load("resources/images/life3.png").convert_alpha()

        # buttons
        self.restart_button = pygame.image.load("resources/images/B_restart.png")
        self.home_button = pygame.image.load("resources/images/B_home.png")

    def create_rect(self):
        """ Create rect
        """

        self.restart_rect = pygame.Rect((0, 610), (100, 30))
        self.quit_game_rect = pygame.Rect((0, 645), (100, 30))

    def display_labyrinth(self):
        """ display labyrinth images
        """
        self.window_surface.blit(self.water_pic, [0, 0])
        line_nbr = 0
        for line in self.labyrinth:
            column_nbr = 0
            for sprite in line:

                column = column_nbr * self.sprite_cote
                line = line_nbr * self.sprite_cote

                if sprite != "w" and sprite != "e":
                    self.window_surface.blit(self.path_pic, [column, line])
                
                if sprite == 'w':
                    self.window_surface.blit(self.wall_pic, [column, line])
                #elif sprite == "e":
                    #self.window_surface.blit(self.water_pic, [column, line])
                elif sprite == "a":
                    self.window_surface.blit(self.gardian, [column, line])
                elif sprite == 'A':
                    self.window_surface.blit(self.armor, [column, line])
                elif sprite == 'H':
                    self.window_surface.blit(self.helmet, [column, line])
                elif sprite == 'D':
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
        if "D" in self.player.inventory:
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
                        self.player.run = "home"

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
        """ Dispaly labyrinth surface
        """

        self.player_pic = self.playerdown
        self.gardian_pic = self.gardian

        pygame.key.set_repeat(100, 70)

        while self.player.run == "game":

            # Display menu
            self.display_menu()

            # Display labytinth
            self.display_labyrinth()

            # player position in pixel
            self.player_position = (
                self.player.player_position[0] * self.sprite_cote, \
                self.player.player_position[1] * self.sprite_cote)

            # display player
            self.window_surface.blit(self.player_pic, self.player_position)

            # Pygame event
            self.pygame_event()

            self.interface = self.player.run

            # Refresh pygame display
            pygame.display.flip()
