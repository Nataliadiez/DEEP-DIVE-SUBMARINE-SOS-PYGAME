import pygame
import sys
from constantes import *
pygame.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
font_input = pygame.font.SysFont("Arial", 50)

ingreso = ""
ingreso_rect = pygame.Rect(200,400,150,40)


reloj = pygame.time.Clock()


correr = True
while correr:
    milis = reloj.tick(20)
    pantalla.fill((COLOR_NEGRO))

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            correr = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                ingreso = ingreso[0:-1]  # Método slice
            elif evento.key == pygame.K_RETURN:
                print("Texto ingresado:", ingreso)
                ingreso = ""
            else:
                ingreso += evento.unicode  # Da el texto que se presiona en el teclado

    pantalla.fill(COLOR_NEGRO)

    pygame.draw.rect(pantalla, COLOR_BLANCO, ingreso_rect, 2)
    font_input_surface = font_input.render(ingreso, True, COLOR_ROJO)
    pantalla.blit(font_input_surface, (ingreso_rect.x + 5, ingreso_rect.y + 5))
    pygame.display.flip()