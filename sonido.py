import pygame

class Sonido_y_musica:
    def __init__(self):
        pygame.mixer.init()
        #CANCIONES
        #Archivo sonido
        self.musica_fondo_lvl1 = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/musica_fondo/Guts Theme (8bit).mp3")
        self.musica_fondo_lvl2 = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/musica_fondo/lvl2.mp3")
        self.musica_fondo_lvl3 = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/musica_fondo/pelea_final.mp3")
        self.musica_fondo_menu = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/musica_fondo/intro_menu.mp3")
        #Volumen
        self.volumen_lvl1 = 0.0
        self.volumen_lvl2 = 0.0
        self.volumen_lvl3 = 0.0
        self.volumen_menu = 0.0
        self.musica_fondo_lvl1.set_volume(self.volumen_lvl1)
        self.musica_fondo_lvl2.set_volume(self.volumen_lvl2)
        self.musica_fondo_lvl3.set_volume(self.volumen_lvl3)
        self.musica_fondo_menu.set_volume(self.volumen_menu)
        #play
        self.musica_fondo_lvl1.play(-1)
        self.musica_fondo_lvl2.play(-1)
        self.musica_fondo_lvl3.play(-1)
        self.musica_fondo_menu.play(-1)

        #EFECTOS DE SONIDO
        #archivos
        self.mordida_tiburon = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/efectos_sonido/shark_bite.mp3")
        self.fuego = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/efectos_sonido/fuego kraken.mp3")
        self.hits_kraken = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/efectos_sonido/hits kraken.mp3")
        self.misil = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/efectos_sonido/misil.mp3")
        self.muerte_kraken = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/efectos_sonido/muerte kraken.mp3")
        self.efecto_agua = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/efectos_sonido/surfswim.wav")
        #volumen
        self.volumen_efecto_agua = 0.0
        self.volumen_mordida = 0.7
        self.volumen_fuego = 0.7
        self.volumen_hits_kraken = 0.7
        self.volumen_misil = 0.7
        self.volumen_muerte_kraken = 0.7
        #seteo de volumen
        self.efecto_agua.set_volume(self.volumen_menu)
        self.mordida_tiburon.set_volume(self.volumen_mordida)
        self.fuego.set_volume(self.volumen_fuego)
        self.misil.set_volume(self.volumen_misil)
        self.muerte_kraken.set_volume(self.volumen_muerte_kraken)
        self.hits_kraken.set_volume(self.volumen_hits_kraken)
        #play
        self.efecto_agua.play(-1)

        
        