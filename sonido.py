import pygame

class Sonido_y_musica:
    def __init__(self):
        pygame.mixer.init()
        self.volumen_lvl1 = 0.0
        self.volumen_menu = 0.0
        self.volumen_mordida = 0.7
        self.volumen_efecto_agua = 0.0
        self.volumen_efecto_muerte_buzo = 0.4
        self.musica_fondo_lvl1 = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/musica_fondo/Guts Theme (8bit).mp3")
        self.musica_fondo_menu = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/musica_fondo/Water Map Theme.wav")
        self.mordida_tiburon = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/efectos_sonido/shark_bite.mp3")
        self.efecto_agua = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/efectos_sonido/surfswim.wav")
        self.efecto_muerte_buzo = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS\sonido\efectos_sonido\Sound effect- screaming girl_FzXTd6mrtmM.mp3")
        self.musica_fondo_lvl1.set_volume(self.volumen_lvl1)
        self.efecto_agua.set_volume(self.volumen_menu)
        self.musica_fondo_menu.set_volume(self.volumen_efecto_agua)
        self.mordida_tiburon.set_volume(self.volumen_mordida)
        self.efecto_muerte_buzo.set_volume(self.volumen_efecto_muerte_buzo)
        self.musica_fondo_lvl1.play()
        self.musica_fondo_menu.play()
        self.efecto_agua.play(-1)
        
        
        """ self.efectos = {
            'mordida_tiburon': mixer.Sound('mordida_tiburon.wav'),
            'agua': mixer.Sound('sonido_agua.wav'),
            'muerte': mixer.Sound('muerte.wav'),
            # Agrega más efectos según sea necesario
        } """

        
        