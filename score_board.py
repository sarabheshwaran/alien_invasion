import pygame 

class Scoreboard():

    def __init__(self, ai_settings, screen, stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 30)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()



    def prep_score(self):

        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(str("Score :" + str(score_str)), True, self.text_color, (0,0,0))
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))

        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(str("High Score :" + str(high_score_str)), True, self.text_color, (0,0,0))

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        self.level_image = self.font.render(str("Level :" + str(self.stats.level)), True, self.text_color, (0,0,0))
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def show_score(self):

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
    