import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self,ai_settings,screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images\spaceship.bmp')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
    
        #Movement
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
    
    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.speed_factor
        elif self.move_left and self.rect.left > 0:
            self.center -= self.ai_settings.speed_factor
        elif self.move_up and self.rect.bottom > 120 :
            self.rect.bottom -= self.ai_settings.speed_factor
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom :
            self.rect.bottom += self.ai_settings.speed_factor
        # Update rect object from self.center.
        self.rect.centerx = self.center
       
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx