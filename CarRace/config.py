import pygame

resolucion_pantalla = {"ancho": 1100, "alto": 700}

screen = pygame.display.set_mode((resolucion_pantalla["ancho"], resolucion_pantalla["alto"]))

pygame.display.set_caption("Car Race")

icono = pygame.image.load(r"Recursos\icono_auto.jpg") 

pygame.display.set_icon(icono)

origen = (0, 0)

clock = pygame.time.Clock()