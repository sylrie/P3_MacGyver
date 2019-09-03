
""" game display
    display game interface
"""
# library imports
import pygame

# programs import
from labyrinth import Labyrinth
from player import Player

class LabyDisplay():
    """ Display laby interface
    """

    def __init__(self, level):

        self.level = level
        self.sprite_cote = 40
        self.active_interface = "game"

        self.init_game() 
        self.create_surface()
        self.loads()
        self.create_rect()
        self.display()

    def init_game(self):
        """ Generate labyrinth and load player values
        """

        self.lab = Labyrinth(self.level)
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

        # Player's images
        self.playerdown = pygame.image.load("resources/images/playerdown.png").convert_alpha()
        self.playerup = pygame.image.load("resources/images/playerup.png").convert_alpha()
        self.playerright = pygame.image.load("resources/images/playerright.png").convert_alpha()
        self.playerleft = pygame.image.load("resources/images/playerleft.png").convert_alpha()
    
        # Gardian's image
        self.gardian_pic = pygame.image.load("resources/images/gardian.png").convert_alpha()
       
        # Wall
        self.wall_pic = pygame.image.load("resources/images/wall.png").convert()
        # Passage
        self.path_pic = pygame.image.load("resources/images/pass.png").convert()
        # water
        self.water_pic = pygame.image.load("resources/images/water2.png").convert()

        # Inventory
        self.inventory_pic =  pygame.image.load("resources/images/inventory2.png")
        # Syringe's images
        self.syringe_pic = pygame.image.load("resources/images/syringe.png").convert_alpha()      
        self.syringe_pic_menu = pygame.image.load("resources/images/syringe2.png").convert_alpha()
      
        # Dropper's images
        self.dropper_pic = pygame.image.load("resources/images/dropper.png").convert_alpha()      
        self.dropper_pic_menu = pygame.image.load("resources/images/dropper2.png").convert_alpha()
      
        # Tube's images
        self.tube_pic = pygame.image.load("resources/images/tube.png").convert_alpha()  
        self.tube_pic_menu = pygame.image.load("resources/images/tube2.png").convert_alpha()
       
        # heart's images
        self.heart_pic = pygame.image.load("resources/images/heart.png").convert_alpha()    
        self.heart_pic_menu = pygame.image.load("resources/images/heart2.png").convert_alpha()
        
        # buttons
        self.restart_button = pygame.image.load("resources/images/B_restart.png")
        self.home_button = pygame.image.load("resources/images/B_home.png")

    def create_rect(self):
        
        self.restart_rect = pygame.Rect((0, 610), (100, 30))
        self.quit_game_rect = pygame.Rect((0, 645), (100, 30))

    def display(self):

        self.player_pic = self.playerdown
        pygame.key.set_repeat(200, 50)

        while self.player.run == "game":

            # Display buttons
            self.window_surface.blit(self.restart_button, (0, 605))
            self.window_surface.blit(self.home_button, (0, 638))
                 
            # Display life
            self.window_surface.blit(self.heart_pic, (540, 615))
            if self.player.health == 0:
                self.window_surface.blit(self.heart_pic_menu, (490, 615))
                self.window_surface.blit(self.heart_pic_menu, (440, 615))
            elif self.player.health == 1:
                self.window_surface.blit(self.heart_pic, (490, 615))
                self.window_surface.blit(self.heart_pic_menu, (440, 615))
            elif self.player.health == 2:
                self.window_surface.blit(self.heart_pic, (490, 615))
                self.window_surface.blit(self.heart_pic, (440, 615))

            # Display inventory
            self.window_surface.blit(self.inventory_pic, (155, 610))
            if "D" in self.player.inventory:
                self.window_surface.blit(self.dropper_pic, (8*self.sprite_cote, 620))
            else:
                self.window_surface.blit(self.dropper_pic_menu, (8*self.sprite_cote, 620))
            if "S" in self.player.inventory:
                self.window_surface.blit(self.syringe_pic, (6*self.sprite_cote, 620))
            else:
                self.window_surface.blit(self.syringe_pic_menu, (6*self.sprite_cote,620))
            if "T" in self.player.inventory:
                self.window_surface.blit(self.tube_pic, (4*self.sprite_cote, 620))
            else:
                self.window_surface.blit(self.tube_pic_menu, (4*self.sprite_cote, 620))

            # Display labytinth
            line_nbr = 0
            for line in self.labyrinth:
                column_nbr = 0
                for sprite in line:
                    x = column_nbr * self.sprite_cote
                    y = line_nbr * self.sprite_cote
                    if sprite != "w":
                        self.window_surface.blit(self.path_pic, [x, y])
                    if sprite == "a":
                        self.window_surface.blit(self.gardian_pic, [x, y])
                    if sprite == 'w':
                        self.window_surface.blit(self.wall_pic, [x, y])
                    if sprite == "e":
                        self.window_surface.blit(self.water_pic, [x, y])
                    if sprite == "H":
                        self.window_surface.blit(self.heart_pic, [x, y])
                    if sprite == 'T':
                        self.window_surface.blit(self.tube_pic, [x, y])
                    if sprite == 'D':
                        self.window_surface.blit(self.dropper_pic, [x, y])
                    if sprite == 'S':
                        self.window_surface.blit(self.syringe_pic, [x, y])
                    column_nbr += 1
                line_nbr += 1

            # Check player position
            self.player_position = (
                self.player.player_position[0] * self.sprite_cote, \
                self.player.player_position[1] * self.sprite_cote)
            # display player
            self.window_surface.blit(self.player_pic, self.player_position)

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
                    
                   
            self.interface = self.player.run     
            # Refresh pygame display
            pygame.display.flip()




