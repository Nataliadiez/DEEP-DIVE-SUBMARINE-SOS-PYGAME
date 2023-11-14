import pygame
from constantes import *

class Auxiliar:
    @staticmethod #se pone metodo estatico para no construir un objeto
    def getSurfaceFromSprite(path,cant_columnas,cant_filas,numero_fila, ancho, alto, color_key=False, color=None):#recorre todas las fotos
        lista = []
        surface_imagen = pygame.image.load(path)
        surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
        fotograma_ancho = int(surface_imagen.get_width()/cant_columnas)
        fotograma_alto = int(surface_imagen.get_height()/cant_filas)
        x = 0
        if color_key:
            surface_imagen.set_colorkey(color)
        for columna in range(cant_columnas):
            for fila in range (cant_filas):
                x = columna * fotograma_ancho
                y = numero_fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho, fotograma_alto)
                lista.append(surface_fotograma)
        return lista
    
    @staticmethod
    def colisiones(pantalla, color):
        #pygame.draw.rect(pantalla, color, buzo.rect, 1)
        #pygame.draw.rect(pantalla, COLOR_ROJO_PAINT, self.rect_colision, 1)
        pass

    @staticmethod
    def personalizar_img(ruta:str, scale=False, ancho=None, alto=None, color_key=False, color=None):
        imagen = pygame.image.load(ruta).convert()
        if scale:
            imagen = pygame.transform.scale(imagen, (ancho, alto))
        if color_key:
            imagen.set_colorkey(color)

        return imagen
    
    @staticmethod
    def dibujar_enemigos(menu:object)->None:
        for i in range (len(menu.nivel_1.lista_tiburones)):
            tiburon = menu.nivel_1.lista_tiburones
            if i <= 2:
                tiburon[i].set_animation(f"{PATH_IMAGE}/enemigos/Shark-Sheet.png", 8, 1, 0, ANCHO_TIBURON,ALTO_TIBURON, False, None)
            else:
                tiburon[i].set_animation(f"{PATH_IMAGE}/enemigos/pez_espada.png", 4, 1, 0, 300, 50, False, None)


    #TODO usar esta lógica para guardar los puntajes en vez de la música
    """ @staticmethod
    def crear_json_musica(path_archivo, musica_fondo):
        # Reemplaza las dobles barras invertidas con una sola
        musica_fondo = musica_fondo.replace("//", "/")

        with open(path_archivo, "w", encoding="utf-8") as archivo:
            dict_musica = {"musica_fondo": musica_fondo}
            json.dump(dict_musica, archivo, indent=4)
        #print(f"Música de fondo: {dict_musica}.")
    @staticmethod
    def leer_json_musica():
        try:
            with open("DEEP DIVE - SUBMARINE SOS/json/musica.json", "r", encoding="utf-8") as archivo:
                contenido = json.load(archivo)
                if nombre_lista in contenido:
                    resultado = contenido[nombre_lista]
                else:
                    print(f"No se encontró la lista: {nombre_lista} en el archivo.")
        except FileNotFoundError:
            print(f"No existe el arhivo")
        except Exception as error:
            print(f"No se pudo leer el archivo\nError: {error}")
        
        return contenido """