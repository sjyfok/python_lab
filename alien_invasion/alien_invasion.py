import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(ai_settings, screen)
	
	bg_color = (230, 230, 230)
	

	while True:
		gf.check_events(ship)
		ship.update()
		#screen.fill(ai_settings.bg_color)
		#ship.blitme()
		gf.update_screen(ai_settings, screen, ship)
		pygame.display.flip()


run_game()
