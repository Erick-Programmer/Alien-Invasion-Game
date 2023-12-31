class Settings():
	"""uma classe para armazenar todas as configurações de Invasão Alienígena."""
	def __init__(self):
		"""inicializa as configurações do jogo."""
		#configurações da tela.
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		
		#configurações da espaçonave.
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		
		#configurações dos projéteis.
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		
		#Configurações dos alienígenas.
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		
		# fleet_direction igual a 1 representa a direita; -1 representa a esquerda.
		self.fleet_direction = 1
