import pygame
import sys
from config import *
import json

def pantalla_final(jugador):
    
    fuente_inicio = pygame.font.Font(None, 32)
    fuente_puntuacion = pygame.font.Font(None, 50)

    
    with open("puntuaciones.json","r") as archivo:
        
        info_lista_dics = json.load(archivo)
        
        lista_ordenada = sorted(info_lista_dics, key = lambda x: x["puntaje"], reverse= True)

    
    puesto = 0
    
    lista_puntajes = [fuente_puntuacion.render("N° | NOMB | PUNT | TIEM ", True, (255,255,255))]

    while puesto < 5:
        
        if jugador == lista_ordenada[puesto]:
            
            color = (255, 0, 0)
            
        else:
            
            color = (255, 255, 255)
        
        mensaje = fuente_puntuacion.render(f" {puesto + 1: <2}|{lista_ordenada[puesto]["nombre"]: >10}|{lista_ordenada[puesto]["puntaje"]}|{lista_ordenada[puesto]["tiempo"]}", True, color)
        puesto += 1
        lista_puntajes.append(mensaje) 
        
    

    reiniciar_partida = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+250, 230, 60)
    volver_inicio = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+350, 230, 60)


    while True:
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                
                return "salir"
            
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if reiniciar_partida.collidepoint(pygame.mouse.get_pos()):
                    
                    return "reiniciar"

                if volver_inicio.collidepoint(pygame.mouse.get_pos()):
                    
                    return "volver_inicio"
                
               
                print(pygame.mouse.get_pos())

        pygame.draw.rect(screen,(65,255,15), reiniciar_partida, 0)
        pygame.draw.rect(screen,(255,30,15), volver_inicio, 0)

        mensaje_reinicio = fuente_inicio.render("REINICIAR PARTIDA", True, (255,255,255))
        mensaje_salir = fuente_inicio.render("VOLVER AL MENU", True, (255,255,255))


        screen.blit(mensaje_reinicio, (reiniciar_partida.x+(reiniciar_partida.width - mensaje_reinicio.get_width())/2,reiniciar_partida.y+(reiniciar_partida.height - mensaje_reinicio.get_height())/2))
        screen.blit(mensaje_salir, (volver_inicio.x+(volver_inicio.width - mensaje_salir.get_width())/2,volver_inicio.y+(volver_inicio.height - mensaje_salir.get_height())/2))

        desvio = 0

        for texto in lista_puntajes:
            
            screen.blit(texto, (450, 100 + desvio))
            desvio += 50
            

        pygame.display.flip()

