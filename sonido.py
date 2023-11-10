import pygame.mixer as mixer

class Sonido_y_musica:
    def __init__(self):
        mixer.init()
        self.musica_fondo = None
        self.volumen = 0.2
        self.efectos = {
            'mordida_tiburon': mixer.Sound('mordida_tiburon.wav'),
            'agua': mixer.Sound('sonido_agua.wav'),
            'muerte': mixer.Sound('muerte.wav'),
            # Agrega más efectos según sea necesario
        }

    def reproducir_musica_fondo(self, archivo):
        self.musica_fondo = mixer.music.load(archivo)
        mixer.music.play(-1)  # Reproducir en bucle

    def reproducir_efecto(self, nombre):
        if nombre in self.efectos:
            self.efectos[nombre].play()

    def detener_musica_fondo(self):
        mixer.music.stop()
    
    """ def setear_volumen(self):
        sonido_fondo.set_volume(volumen) """
