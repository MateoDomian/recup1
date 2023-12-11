import pygame
from pygame.locals import *
import sys
import random
from config import *
import json

def juego(nombre):
    
    pygame.init()

    ##########CONFIG 
    juego = True

    pantalla_derrota = False # Bandera derrota

    ##########VARIABLES
    flecha_arriba = False
    flecha_abajo = False
    flecha_derecha = False
    flecha_izquierda = False

    velocidad = 5

    vidas = 3

    mensaje_error = print("ERROR AL CARGAR LA IMAGEN")

    ##########IMAGEN FONDO
    try:
        imagen_fondo_juego = pygame.image.load(r"./Recursos\carretera.png")
        imagen_fondo_juego = pygame.transform.scale(imagen_fondo_juego, (resolucion_pantalla["ancho"], resolucion_pantalla["alto"]))
    except:
        mensaje_error

    

    pos_fondo = 0
    pos_vuelta = -700
    velocidad_fondo = 15

    #vidas
    try:
        imagen_corazon_1 = pygame.image.load(r"./Recursos\corazon.png")
        imagen_corazon_1 = pygame.transform.scale(imagen_corazon_1, (50, 50))
    except:
        mensaje_error

    ##########PANTALLA DERROTA
    reiniciar_partida = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+250, 230, 60)
    salir_del_juego = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+350, 230, 60)
    fuente_inicio = pygame.font.Font(None, 32)

    ##########AUTO MAIN
    imagen_auto_amarillo = pygame.image.load(r"./Recursos\auto_amarillo.png")
    imagen_auto_amarillo = pygame.transform.scale(imagen_auto_amarillo, (resolucion_pantalla["ancho"]/14, resolucion_pantalla["alto"]/6))
    auto_amarillo_rect = imagen_auto_amarillo.get_rect()

    auto_amarillo_rect.bottomleft = ((resolucion_pantalla["ancho"]//2, resolucion_pantalla["alto"]-50))

    def movimiento_auto(rect, izquierda, derecha, arriba, abajo):
        if (izquierda and not derecha):
            rect.x -= velocidad

        if (derecha and not izquierda):
            rect.x += velocidad

        if (arriba and not abajo):
            rect.y -= velocidad

        if (abajo and not arriba):
            rect.y += velocidad
    
    def limites_auto(rect):
        limite = 0
        
        if rect.x <= 180:
            limite = 1
        
        if rect.x >= 850:
            limite = 2
        
        if rect.y <= 0:
            limite = 3
        
        if rect.y >= 580:
            limite = 4

        return limite
    
    ########## ENEMIGOS
    autos_enemigos = []

    imagen_auto_enemigo = pygame.image.load(r"./Recursos\auto_blanco.png")
    imagen_auto_enemigo = pygame.transform.scale(imagen_auto_enemigo, (resolucion_pantalla["ancho"]/14, resolucion_pantalla["alto"]/6))
    imagen_auto_enemigo_rect = imagen_auto_enemigo.get_rect()

    #########
    def agregar_enemigos(autos_enemigos, puntaje):
        
        imagen_auto_enemigo = pygame.image.load(r"./Recursos\auto_blanco.png")
        imagen_auto_enemigo = pygame.transform.scale(imagen_auto_enemigo, (resolucion_pantalla["ancho"]/14, resolucion_pantalla["alto"]/6))
        imagen_auto_enemigo_rect = imagen_auto_enemigo.get_rect()
        auto_x = random.randint(0, 3) * 165 + 260

        aumento_velocidad =  puntaje // 200 * 5 
            
        velocidad = random.randint(10, 15) + aumento_velocidad


        imagen_auto_enemigo_rect.bottomleft = (auto_x, 1)
        autos_enemigos.append({"rect": imagen_auto_enemigo_rect, "velocidad": velocidad})
        
        

        return autos_enemigos

    imagen_disco = pygame.image.load(r"./Recursos\disco_cap_america.png")
    imagen_disco = pygame.transform.scale(imagen_disco, (50, 50))
    imagen_disco_rect = imagen_disco.get_rect()
    imagen_disco_rect.center = (-10, -10)

    timer_autos = pygame.USEREVENT+1
    pygame.time.set_timer(timer_autos, 500)

    timer_segundos = pygame.USEREVENT+2
    pygame.time.set_timer(timer_segundos, 1000)

    cantidad_segundos = 0 

    choco = False  

    disparo_cooldown = 10000
    ultimo_disparo = -10000
    velocidad_disparo = 15

    fuente = pygame.font.Font(None, 60)

    numero_cooldown = 0

    disparo_listo = fuente.render("Disparo Listo", True, (255,0,0))

    puntaje = 0
    
    

    ########## WHILE
    while juego:
        clock.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:

                return {"msg": "salir"}
                
            if evento.type == timer_autos:
                
                autos_enemigos = agregar_enemigos(autos_enemigos, puntaje)
            
            if evento.type == timer_segundos:
                
                cantidad_segundos += 1
                numero_cooldown -= 1
                puntaje += 10
            
            if evento.type == KEYDOWN:    
                
                if evento.key == K_UP:
                    flecha_arriba = True
                if evento.key == K_LEFT:
                    flecha_izquierda = True
                if evento.key == K_RIGHT:
                    flecha_derecha = True
                if evento.key == K_DOWN:
                    flecha_abajo = True
                    
                if evento.key == K_SPACE:

                    tiempo_actual = pygame.time.get_ticks()
                    
                    if (tiempo_actual - ultimo_disparo) >= disparo_cooldown:
                        
                        imagen_disco_rect.center = auto_amarillo_rect.center
                        
                        ultimo_disparo = pygame.time.get_ticks()
                        
                        numero_cooldown = 10

            if evento.type == KEYUP:
                if evento.key == K_UP:
                    flecha_arriba = False
                if evento.key == K_LEFT:
                    flecha_izquierda = False
                if evento.key == K_RIGHT:
                    flecha_derecha = False
                if evento.key == K_DOWN:
                    flecha_abajo = False

        minutos = cantidad_segundos // 60
        segundos = cantidad_segundos - (minutos * 60)
        texto_temporizador = fuente.render(f"{minutos}:{segundos}", True, (255,0,0))

        pos_vuelta += velocidad_fondo
        pos_fondo += velocidad_fondo

        if pos_fondo >= resolucion_pantalla["alto"]:
            pos_fondo = -resolucion_pantalla["alto"]

        if pos_vuelta >= resolucion_pantalla["alto"]:
            pos_vuelta = -resolucion_pantalla["alto"]

        screen.blit(imagen_fondo_juego, (0, pos_fondo))
        screen.blit(imagen_fondo_juego, (0, pos_vuelta))            
        
        cantidad_autos =  len(autos_enemigos)

        indice = 0
        lista_actualizada = []
        
        imagen_disco_rect.y -= velocidad_disparo
                
        while indice < cantidad_autos:
            
            auto = autos_enemigos[indice]

            auto["rect"].y += auto["velocidad"]

            if (not (auto_amarillo_rect.colliderect(auto["rect"])) and auto["rect"].y < resolucion_pantalla["alto"]) and (not (auto["rect"].colliderect(imagen_disco_rect))):
                lista_actualizada.append(auto)
            else:
                choco = True

            if auto_amarillo_rect.colliderect(auto["rect"]):
                
                vidas -= 1
                
                if vidas < 1:
                    
                    with open("puntuaciones.json","r") as archivo:
        
                        info_lista_dics = json.load(archivo)
                        
                    nuevo_jugador = {"nombre": nombre, "puntaje": puntaje, "tiempo": f"{minutos}:{segundos}"}
                    
                    info_lista_dics.append(nuevo_jugador)
                    
                    with open("puntuaciones.json","w") as archivo:
                        
                        json.dump(info_lista_dics, archivo, indent=2)
                    
                    return {"msg": "derrota", "jugador_derrota": nuevo_jugador}

            if auto["rect"].colliderect(imagen_disco_rect):
                puntaje += 50

            indice += 1

            screen.blit(imagen_auto_enemigo, (auto["rect"]))

        autos_enemigos = lista_actualizada

        movimiento_auto(auto_amarillo_rect, flecha_izquierda, flecha_derecha, flecha_arriba, flecha_abajo)    

        limite = limites_auto(auto_amarillo_rect)    

        if limite == 1:
            flecha_izquierda = False

        if limite == 2:
            flecha_derecha = False

        if limite == 3:
            flecha_arriba = False

        if limite == 4:
            flecha_abajo = False

        screen.blit(imagen_auto_amarillo, auto_amarillo_rect)
        screen.blit(imagen_disco, imagen_disco_rect)      
        screen.blit(texto_temporizador, (70, 30))
        texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, (255,0,0))
        screen.blit(texto_puntaje, (70, 110))
        screen.blit(imagen_corazon_1, (870, 30))
        texto_vidas = fuente.render(f"x{vidas}", True, (255, 0, 0))

        screen.blit(texto_vidas, (930, 30))
        
        if numero_cooldown > 0:
            texto_cooldown = fuente.render(f"Proximo Disparo: {numero_cooldown}", True, (255,0,0))    
            screen.blit(texto_cooldown, (70, 70))

        else:
            screen.blit(disparo_listo, (70, 70))

        pygame.display.flip()

        while pantalla_derrota:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pantalla_derrota = False

                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if reiniciar_partida.collidepoint(pygame.mouse.get_pos()):
                        juego = True
                        pantalla_derrota = False

                    if salir_del_juego.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()

            pygame.draw.rect(screen,(65,255,15), reiniciar_partida, 0)
            pygame.draw.rect(screen,(255,30,15), salir_del_juego, 0)

            mensaje_reinicio = fuente_inicio.render("REINICIAR PARTIDA", True, (255,255,255))
            mensaje_salir = fuente_inicio.render("SALIR DEL JUEGO", True, (255,255,255))

            screen.blit(mensaje_reinicio, (reiniciar_partida.x+(reiniciar_partida.width - mensaje_reinicio.get_width())/2,reiniciar_partida.y+(reiniciar_partida.height - mensaje_reinicio.get_height())/2))
            screen.blit(mensaje_salir, (salir_del_juego.x+(salir_del_juego.width - mensaje_salir.get_width())/2,salir_del_juego.y+(salir_del_juego.height - mensaje_salir.get_height())/2))

            pygame.display.flip()

    pygame.quit()
