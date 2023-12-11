import pygame
import time
from config import *
import sys   
from toda_logica import *
from pantalla_fin import *

pygame.init()

fondo = pygame.image.load(r"./Recursos\autopista.jpg")
fondo = pygame.transform.scale(fondo, (resolucion_pantalla["ancho"], resolucion_pantalla["alto"]))

iniciar_partida = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+50, 230, 60)
salir_del_juego = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+150, 230, 60)

fuente_inicio = pygame.font.Font(None, 32)
fuente_nombre = pygame.font.Font(None, 150)

def pintar_menu(nombre):

    while True:
            
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                
                return "salir"

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if iniciar_partida.collidepoint(pygame.mouse.get_pos()):
                    return "juego"


                if salir_del_juego.collidepoint(pygame.mouse.get_pos()):
                    return "salir"
        
        screen.blit(fondo, origen)
        
        pygame.draw.rect(screen,(65,205,15), iniciar_partida, 0)

        pygame.draw.rect(screen,(205,30,15), salir_del_juego, 0)
        
        nombre_pj = fuente_nombre.render(nombre, True, (255,0,0))
        mensaje_inicio = fuente_inicio.render("INICIAR PARTIDA", True, (255,255,255))
        mensaje_salir = fuente_inicio.render("SALIR DEL JUEGO", True, (255,255,255))

        screen.blit(nombre_pj, (450, 125))
        screen.blit(mensaje_inicio, (iniciar_partida.x+(iniciar_partida.width - mensaje_inicio.get_width())/2,iniciar_partida.y+(iniciar_partida.height - mensaje_inicio.get_height())/2))
        screen.blit(mensaje_salir, (salir_del_juego.x+(salir_del_juego.width - mensaje_salir.get_width())/2,salir_del_juego.y+(salir_del_juego.height - mensaje_salir.get_height())/2))

        pygame.display.flip() 

def pantalla_nombre():
    
    fuente_nombre = pygame.font.Font(None, 350)
    fuente_input = pygame.font.Font(None, 60)
    
    nombre = ""
    
    while True:
        
        for evento in pygame.event.get():
            
            if evento.type == pygame.KEYDOWN:
            
                if evento.unicode.isalpha():
                
                    nombre += evento.unicode.upper()
            
            if evento.type == pygame.QUIT:
                
                return "salir"

        nombre_texto = fuente_nombre.render(nombre, True, (255,255,255)) 
        screen.blit(nombre_texto, (250,250))

        input_texto = fuente_input.render("Usuario, ingrese 3 digitos para su nombre", True, (255,255,255))
        screen.blit(input_texto, (150,150))
        pygame.display.flip()  
        
        if len(nombre) == 3:
            
            time.sleep(2)
            return nombre


corriendo_aplicacion = True
pantalla_actual = "nombre"


while corriendo_aplicacion:

    if pantalla_actual == "nombre":

        nombre = pantalla_nombre()
        
        if nombre == "salir":
            
            corriendo_aplicacion = False
            
        else:
            
            pantalla_actual = "inicio"
    
    
    


    if pantalla_actual == "juego":
        
        respuesta = juego(nombre)
            
        if respuesta["msg"] == "salir":
            
            corriendo_aplicacion = False
            
        if respuesta["msg"] == "derrota":
            
            pantalla_actual = "derrota"
            
            jugador = respuesta["jugador_derrota"]
    
    if pantalla_actual == "inicio":
        
        respuesta = pintar_menu(nombre)
        
        if respuesta == "juego":
            
            pantalla_actual = "juego"
            
        if respuesta == "salir":
            
            corriendo_aplicacion = False
        
    elif pantalla_actual == "derrota":
        
        respuesta = pantalla_final(jugador)
        
        if respuesta == "reiniciar":
            
            pantalla_actual = "juego"
            
        elif respuesta == "volver_inicio":    
    
            pantalla_actual = "inicio"
            
        elif respuesta == "salir":
            
            corriendo_aplicacion = False
    
    pygame.display.flip()

pygame.quit()
sys.exit()
