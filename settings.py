import pygame
import random

class settings():
    """class to store settings"""
    def __init__(self):
        """initialize settings"""
        #screen settings
         
        self.width = 1280
        self.height = 720
        self.bg_color = (230,230,230)
        
        #ship settings
        self.speed_factor = 1.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 3
        self.bullet_width = 1
        self.bullet_height = 20
        self.bullet_color = (230,0,0)
        self.bullet_limit = 5

        #sound settings
        self.trigger = pygame.mixer.Sound("images\gun.wav")
        self.shot = pygame.mixer.Sound("images\crash.wav")
        self.click = pygame.mixer.Sound("images\click.wav")

        #alien settings
        self.alien_speed = 1
        self.fleet_drop = 10

        self.list = [1, -1]

        self.fleet_direction = random.choice(self.list)