import pygame

# Inicializamos los modulos de pygame
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((500,368))

# Establecer el título de la ventana
pygame.display.set_caption("Pygame bandera de Grecia")

# Definir colores
blanco = (255, 255, 255)
azul = (0, 0, 255)
azul = (0, 0, 255)
azul = (0, 0, 255)
azul = (0, 0, 255)
azul = (0, 0, 255)
azul = (0, 0, 255)
azul = (0, 0, 255)
azul = (0, 0, 255)
azul = (0, 0, 255)
azul = (0, 0, 255)
azul = (0, 0, 255)




# Creame una superficie
superficie_1 = pygame.Surface((500,400))
superficie_2 = pygame.Surface((65, 65))
superficie_3 = pygame.Surface((65, 65))
superficie_4 = pygame.Surface((65, 65))
superficie_5 = pygame.Surface((65, 65))
superficie_6 = pygame.Surface((400, 35))
superficie_7 = pygame.Surface((400, 35))
superficie_8 = pygame.Surface((400, 35))
superficie_9 = pygame.Surface((500, 35))
superficie_10 = pygame.Surface((500, 35))
superficie_11 = pygame.Surface((500, 35))
superficie_12 = pygame.Surface((500, 35))



# Rellenamos la superficie de color 
superficie_1.fill(blanco)
superficie_2.fill(azul)
superficie_3.fill(azul)
superficie_4.fill(azul)
superficie_5.fill(azul)
superficie_6.fill(azul)
superficie_7.fill(azul)
superficie_8.fill(azul)
superficie_9.fill(azul)
superficie_10.fill(azul)
superficie_11.fill(azul)
superficie_12.fill(azul)



# agregar o mover la superficie a la ventana
ventana.blit(superficie_1, (0, 0))
ventana.blit(superficie_2, (0, 0))
ventana.blit(superficie_3, (0, 100))
ventana.blit(superficie_4, (100, 100))
ventana.blit(superficie_5, (100, 0))
ventana.blit(superficie_6, (165, 65))
ventana.blit(superficie_7, (150, 0))
ventana.blit(superficie_8, (150, 130))
ventana.blit(superficie_9, (0, 195))
ventana.blit(superficie_10, (0, 265))
ventana.blit(superficie_11, (0, 335))
ventana.blit(superficie_12, (0, 405))



# Actualizar la pantalla
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()

