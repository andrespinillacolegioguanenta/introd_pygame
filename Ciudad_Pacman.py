# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.

# importamos la libreria pygame
import pygame
import sys
import math

# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((600, 600))

# establecer titulo de la ventana
pygame.display.set_caption("Dibujar formas basicas")

# definición colores
negro = (0, 0, 0)
rojo = (255,0,0)
azul = (0,0,255)
naranja = (255, 165, 0)
Amarillo = (255, 255, 0)
fusia = (255, 0, 255)
verde = (0, 255, 0)
blanco = (255, 255, 255)
cian = (0, 255, 255)
morado = (128, 0, 128)

# variables auxiliares
PI = math.pi

# Objeto para la gestión del tiempo
clock = pygame.time.Clock()


# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(50)

    for event in pygame.event.get():
        # Al hacer click sobre el botón de cerrar la ventana, el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(blanco)

    #---------------------------------
    # Dibujar formulas con modulo draw
    #---------------------------------

    pygame.draw.circle(ventana, negro, (300, 300), 75, 3)
    pygame.draw.line(ventana, rojo, (247, 247), (351, 351), 3)
    pygame.draw.line(ventana, rojo, (250, 350), (351, 247), 3)
    pygame.draw.line(ventana, rojo, (300, 224), (300, 376), 3)
    pygame.draw.line(ventana, rojo, (224, 300), (376, 300), 3)
    pygame.draw.line(ventana, negro, (351, 351), (375, 400), 6)
    pygame.draw.line(ventana, negro, (250, 350), (235, 400), 6)


    # actualizar visualización de la ventana
    pygame.display.flip()
