import sys
import pygame
import ship
import settings
from bullet import Bullet

class key_check :
    
    
    def check_keydown (event, ai_settings, screen, ship, bullets):
        
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            ship.move_right = True
        elif event.key == pygame.K_LEFT:
            ship.move_left = True
        elif event.key == pygame.K_UP:
            ship.move_up = True
        elif event.key == pygame.K_DOWN:
            ship.move_down = True
        elif event.key == pygame.K_SPACE:
            Bullet.fire_bullet(ai_settings,screen,ship,bullets)
        elif event.key == pygame.K_q:
            sys.exit()
    
    def check_keyup (event,ship):
        
        if event.key == pygame.K_RIGHT:
            ship.move_right = False 
        elif event.key == pygame.K_LEFT:
            ship.move_left = False
        elif event.key == pygame.K_UP:
            ship.move_up = False
        elif event.key == pygame.K_DOWN:
            ship.move_down = False

    