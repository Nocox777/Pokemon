import pygame
import pokemon


pygame.init()

# Ventana
ANCHO, ALTO = 1000, 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Selección Pokémon")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# Fondos
fondo_menu = pygame.image.load("fondo1.jpg").convert()
fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO, ALTO))
fondo_juego = pygame.image.load("fondo2.png").convert()
fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO, ALTO))
fondo_pelea = pygame.image.load("fondo_pelea.jpg").convert()
fondo_pelea = pygame.transform.scale(fondo_pelea, (ANCHO, ALTO))

# Pokémon
charmander_img = pygame.transform.scale(pygame.image.load("charmander.png"), (200, 200))
squirtle_img = pygame.transform.scale(pygame.image.load("squirtle.png"), (200, 200))
bulbasaur_img = pygame.transform.scale(pygame.image.load("bulbasaur.png"), (200, 200))

c_pelea1 = pygame.transform.scale(pygame.image.load("c_pelea1.png"), (200, 200))
b_pelea1 = pygame.transform.scale(pygame.image.load("b_pelea1.png"), (200, 200))
s_pelea1 = pygame.transform.scale(pygame.image.load("s_pelea1.png"), (200, 200))

c_pelea2 = pygame.transform.scale(pygame.image.load("c_pelea2.png"), (200, 200))
b_pelea2 = pygame.transform.scale(pygame.image.load("b_pelea2.png"), (200, 200))
s_pelea2 = pygame.transform.scale(pygame.image.load("s_pelea2.png"), (200, 200))


tipo_fuego= pygame.transform.scale(pygame.image.load("Fuego.png"),(140,50))
tipo_agua= pygame.transform.scale(pygame.image.load("Agua.png"),(140,50))
tipo_planta= pygame.transform.scale(pygame.image.load("Planta.png"),(140,50))

pygame.display.set_caption("Texto Pixel Art")
fuente = pygame.font.SysFont("PressStart2P.ttf", 30)

# Botones menú inicial
botones = [
    [charmander_img, 120, 400],
    [squirtle_img, 420, 400],
    [bulbasaur_img, 720, 400]
]
nombres = ["Charmander", "Squirtle", "Bulbasaur"]

# Botones segunda pantalla
opciones = ["PELEAR", "SALIR"]

# Estados

pantalla_menu = 0
seleccion_pokemon = 0
seleccion_opcion = 0
pokemon_elegido = None
pokemon_enemigo= None

jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

        elif evento.type == pygame.KEYDOWN:
            if pantalla_menu==0:
                if evento.key == pygame.K_LEFT:
                    seleccion_pokemon = (seleccion_pokemon - 1) % len(botones)
                elif evento.key == pygame.K_RIGHT:
                    seleccion_pokemon = (seleccion_pokemon + 1) % len(botones)
                elif evento.key == pygame.K_RETURN:
                    pokemon_elegido = seleccion_pokemon
                    pantalla_menu = 1 
                    
            elif pantalla_menu==1:
                if evento.key == pygame.K_UP:
                    seleccion_opcion = (seleccion_opcion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion_opcion = (seleccion_opcion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if seleccion_opcion == 0:  # PELEAR
                        pantalla_menu=2  # Aquí iría la pantalla de batalla
                    elif seleccion_opcion == 1:  # SALIR
                        jugando = False
                        
            elif pantalla_menu==2:
                if evento.key == pygame.K_LEFT:
                    seleccion_pokemon = (seleccion_pokemon - 1) % len(botones)
                elif evento.key == pygame.K_RIGHT:
                    seleccion_pokemon = (seleccion_pokemon + 1) % len(botones)
                elif evento.key == pygame.K_RETURN:
                    pokemon_enemigo = seleccion_pokemon
                    pantalla_menu = 3
                        

    if pantalla_menu==0:
        ventana.blit(fondo_menu, (0, 0))
        for i, (imagen, x, y) in enumerate(botones):
            ventana.blit(imagen, (x, y))
            if i == seleccion_pokemon:
                pygame.draw.rect(ventana, ROJO, (x-5, y-5, imagen.get_width()+10, imagen.get_height()+10), 3)
        
    elif pantalla_menu==1:
        
        ventana.blit(fondo_juego, (0, 0))
        if pokemon_elegido == 0:
            ventana.blit(charmander_img, (80, 180))
            ventana.blit(tipo_fuego, (400,290))
            for i in range(6):  
             texto=fuente.render(f"{pokemon.stats[i]}{pokemon.stats1[i]}",True,ROJO)
             ventana.blit(texto, (400,450+i*30))
             
        elif pokemon_elegido == 1:
            ventana.blit(squirtle_img, (80, 180))
            ventana.blit(tipo_agua, (400,290))
            for i in range(6):  
             texto=fuente.render(f"{pokemon.stats[i]}{pokemon.stats2[i]}",True,ROJO)
             ventana.blit(texto, (400,450+i*30))
             
        elif pokemon_elegido == 2:
            ventana.blit(bulbasaur_img, (80, 180))
            ventana.blit(tipo_planta, (400,290))
            for i in range(6):  
             texto=fuente.render(f"{pokemon.stats[i]}{pokemon.stats3[i]}",True,ROJO)
             ventana.blit(texto, (400,450+i*30))
            

        # Mostrar botones PELEAR/SALIR
        for i, texto_op in enumerate(opciones):
            color = ROJO if i == seleccion_opcion else NEGRO
            texto_render = fuente.render(texto_op, False, color)
            ventana.blit(texto_render, (80, 600 + i * 50))
            
            
    elif pantalla_menu==2:
        ventana.blit(fondo_menu, (0, 0))
        texto=fuente.render("Elegir rival",True,NEGRO)
        ventana.blit(texto, (480,100))
        for i, (imagen, x, y) in enumerate(botones):
            ventana.blit(imagen, (x, y))
            if i == seleccion_pokemon:
                pygame.draw.rect(ventana, ROJO, (x-5, y-5, imagen.get_width()+10, imagen.get_height()+10), 3)
                
    elif pantalla_menu==3:
        ventana.blit(fondo_pelea, (0, 0))
        if pokemon_elegido ==0:
         ventana.blit(c_pelea1, (150, 360))
        elif pokemon_elegido==1:
         ventana.blit(s_pelea1,(150, 360))
        else:
         ventana.blit(b_pelea1,(150, 360))
         
        if pokemon_enemigo==0:
           ventana.blit(c_pelea2, (630, 150)) 
        elif pokemon_enemigo==1:
            ventana.blit(s_pelea2, (630, 150)) 
        else: 
            ventana.blit(b_pelea2, (630, 150))
        
        
        
    

    pygame.display.update()

pygame.quit()
