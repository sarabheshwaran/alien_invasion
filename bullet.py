import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):

        super(Bullet,self).__init__()
        self.screen = screen
        
        self.bg = pygame.image.load('images\laser.bmp')
        self.b_img = pygame.transform.scale(self.bg,(30,30))
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height )
        self.rect.centerx = ship.rect.centerx - 13
        self.rect.top = ship.rect.top
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.b_img,self.rect)


    def fire_bullet(ai_settings, screen, ship, bullets):
        """fire a bullet if limit satisfied"""
        if len(bullets) < ai_settings.bullet_limit:
                new_bullet = Bullet(ai_settings,screen,ship)
                bullets.add(new_bullet)
                ai_settings.trigger.play()