from constantes import *
import pygame

segundos = "12"
fin_tiempo = False

pygame.init()
#definit timer
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos, 1000)
#musica
pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("DEEP DIVE - SUBMARINE SOS/sonido/Guts Theme (8bit).mp3")
volumen = 0.10
sonido_fondo.set_volume(volumen)
#pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
#texto para renderizar el tiempo
fuente = pygame.font.SysFont("Arial", 80)
correr = True
while correr:
    sonido_fondo.play()
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            correr = False
        if evento.type == pygame.USEREVENT:
            if evento.type == timer_segundos:
                if fin_tiempo == False:
                    segundos = int(segundos) - 1
                    volumen -= 0.01
                    sonido_fondo.set_volume(volumen)
                    if int(segundos) == 0:
                        fin_tiempo = True
                        segundos = "Fin del tiempo"
                        sonido_fondo.stop()
    pantalla.fill(COLOR_NEGRO)
    segundos_texto = fuente.render(str(segundos), True, COLOR_BLANCO)
    pantalla.blit(segundos_texto, (340,10))
    pygame.display.flip()

sonido_fondo.stop()
pygame.quit()

    
