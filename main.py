import sys
import pygame
from pygame.sprite import Group

from settings import settings
from game_stats import GameStats
from score_board import Scoreboard
from button import Button
from ship import Ship 
from alien import Alien
import event_checker as gf
from bullet import Bullet

def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    bg = pygame.image.load('images\space.bmp')
    bg_image = pygame.transform.scale(bg,(1280,720))
    
    # make a ship
    ship = Ship(ai_settings,screen)
    
    #make group to store bullets 
    bullets = Group()
    aliens = Group()
    alien = Alien(ai_settings,screen)
    

    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    # Start the main loop for the game.
    while True:
        screen.blit(bg_image,(0,0))
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
        
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
    
run_game() 