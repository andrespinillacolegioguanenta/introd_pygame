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
pygame.display.set_caption("Parque de Atracciones")

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
marron = (165, 42, 42)
verde_oscuro = (0, 100, 0)
cafe = (139, 69, 19)
celeste = (135, 206, 235)

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

    ventana.fill(celeste)
    #---------------------------------
    # Dibujar formulas con modulo draw
    #---------------------------------
    
    # Rueda de la fortuna
    pygame.draw.circle(ventana, negro, (300, 300), 75, 3)
    pygame.draw.line(ventana, rojo, (247, 247), (351, 351), 3)
    pygame.draw.line(ventana, rojo, (250, 350), (351, 247), 3)
    pygame.draw.line(ventana, rojo, (300, 224), (300, 376), 3)
    pygame.draw.line(ventana, rojo, (224, 300), (376, 300), 3)
    pygame.draw.line(ventana, negro, (351, 351), (375, 400), 6)
    pygame.draw.line(ventana, negro, (250, 350), (235, 400), 6)
    pygame.draw.rect(ventana, negro, (228, 400, 154, 50))
    fuente_arial = pygame.font.SysFont("Arial", 20, 1, 1)
    texto = fuente_arial.render("Rueda fortuna", 1, negro)
    ventana.blit(texto, (240, 207))

    # montaña rusa 
    pygame.draw.line(ventana, naranja, (600, 0), (450, 150), 3)
    pygame.draw.line(ventana, naranja, (100, 100), (450, 150), 3)
    pygame.draw.line(ventana, naranja, (500, 0), (400, 90), 3)
    pygame.draw.line(ventana, naranja, (100, 50), (400, 90), 3)
    pygame.draw.rect(ventana, verde, (0, 50, 100, 100))
    pygame.draw.polygon(ventana, fusia, [(0, 50), (50, 0), (100, 50)])
    pygame.draw.rect(ventana, verde_oscuro, (10, 100, 80, 40))
    pygame.draw.line(ventana, marron, (490, 10), (585, 15), 3)
    pygame.draw.line(ventana, marron, (470, 30), (560, 40), 3)
    pygame.draw.line(ventana, marron, (444, 50), (535, 65), 3)
    pygame.draw.line(ventana, marron, (418, 70), (510, 90), 3)
    pygame.draw.line(ventana, marron, (400, 90), (450, 150), 3)
    pygame.draw.line(ventana, marron, (410, 80), (480, 120), 3)
    pygame.draw.line(ventana, marron, (376, 87), (380, 141), 3)
    pygame.draw.line(ventana, marron, (343, 83), (337, 133), 3)
    pygame.draw.line(ventana, marron, (313, 80), (310, 128), 3)
    pygame.draw.line(ventana, marron, (283, 77), (280, 128), 3)
    pygame.draw.line(ventana, marron, (253, 72), (250, 124), 3)
    pygame.draw.line(ventana, marron, (223, 67), (220, 120), 3)
    pygame.draw.line(ventana, marron, (193, 62), (190, 115), 3)
    pygame.draw.line(ventana, marron, (163, 57), (160, 110), 3)
    pygame.draw.line(ventana, marron, (133, 52), (130, 105), 3)
    texto = fuente_arial.render("Montaña", 1, negro)
    ventana.blit(texto, (0, 50))
    texto = fuente_arial.render("Rusa", 1, negro)
    ventana.blit(texto, (0, 70))

    # Puesto de comida
    pygame.draw.rect(ventana, rojo, (0, 500, 120, 100))
    pygame.draw.rect(ventana, blanco, (7, 515, 106, 40))
    pygame.draw.polygon(ventana,azul, [(0, 500), (60, 450), (120, 500)])
    texto = fuente_arial.render("Puesto de ", 1, negro)
    ventana.blit(texto, (0, 565))
    texto = fuente_arial.render("Comida", 1, negro)
    ventana.blit(texto, (0, 585))

    # Muro de escalar 
    pygame.draw.rect(ventana, marron, (450, 400, 150, 200))
    pygame.draw.circle(ventana, blanco, (500, 420), 10)
    pygame.draw.circle(ventana, blanco, (510, 450), 10)
    pygame.draw.circle(ventana, blanco, (490, 500), 10)
    pygame.draw.circle(ventana, blanco, (510, 570), 10)
    pygame.draw.circle(ventana, blanco, (550, 500), 10)
    pygame.draw.circle(ventana, blanco, (570, 470), 10)
    pygame.draw.circle(ventana, blanco, (590, 415), 10)
    pygame.draw.circle(ventana, blanco, (583, 590), 10)
    texto = fuente_arial.render("Muro de Escalar", 1, negro)
    ventana.blit(texto, (440, 380))

    # Autor
    texto = fuente_arial.render("Andres Pinilla", 1, negro)
    ventana.blit(texto, (0, 300))
    # actualizar visualización de la ventana
    pygame.display.flip()
