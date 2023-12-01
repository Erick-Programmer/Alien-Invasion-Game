import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import Game_stats
from button import Button

def run_game():
	#inicializa o pygame, as configurações e o objeto screen (display).
	pygame.init()
	ai_settings = Settings()
	
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
 
	pygame.display.set_caption("Alien Invasion")
 
	# Cria o botão Play
	play_button = Button(ai_settings, screen, "Play")
 
	# Cria uma instância para armazenar dados estatísticos do jogo
	stats = Game_stats(ai_settings)
		
	#cria uma espaçonave (objeto).
	ship = Ship(ai_settings, screen)
	
	#criamos um grupo onde serão armazenados os projéteis.
	bullets = Group()
	
	#criamos um grupo de alienigenas.
	aliens = Group()
	
	#criamos a frota de alienigena.
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#inicializa o laço principal do jogo.
	while True:
		#observa eventos do teclado e de mouse.
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats,screen, ship, aliens, bullets)
			
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()


#pagina 345!
