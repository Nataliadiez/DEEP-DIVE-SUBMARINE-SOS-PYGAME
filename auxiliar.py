import pygame

class Auxiliar:
    @staticmethod #se pone metodo estatico para no construir un objeto
    def getSurfaceFromSprite(path,cant_columnas,cant_filas,numero_fila, ancho, alto):#recorre todas las fotos
        lista = []
        surface_imagen = pygame.image.load(path)
        surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
        fotograma_ancho = int(surface_imagen.get_width()/cant_columnas)
        fotograma_alto = int(surface_imagen.get_height()/cant_filas)
        x = 0
        for columna in range(cant_columnas):
            for fila in range (cant_filas):
                x = columna * fotograma_ancho
                y = numero_fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho, fotograma_alto)
                lista.append(surface_fotograma)
        return lista
    
    @staticmethod
    def rectangulos(pantalla, color):
        pass