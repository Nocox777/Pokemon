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

fondo_menu = pygame.image.load("fondo1.jpg").convert()
fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO, ALTO))

fondo_juego = pygame.image.load("fondo2.png").convert()
fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO, ALTO))

# Cargar imágenes (usa las tuyas con fondo transparente)
charmander_img = pygame.image.load("charmander.png")
squirtle_img = pygame.image.load("squirtle.png")
bulbasaur_img = pygame.image.load("bulbasaur.png")

# Escalar si es necesario
charmander_img = pygame.transform.scale(charmander_img, (200, 200))
squirtle_img = pygame.transform.scale(squirtle_img, (200, 200))
bulbasaur_img = pygame.transform.scale(bulbasaur_img, (200, 200))

fuente = pygame.font.SysFont("Arial", 30)

opciones= [fuente.render("PELEAR",True,ROJO), fuente.render("SALIR",True,ROJO)]



# Lista de botones (imagen, x, y)
botones = [
    [charmander_img, 120, 400],
    [squirtle_img, 420, 400],
    [bulbasaur_img, 720, 400]
]

# Índice seleccionado
seleccion_accion=0
seleccion = 0
en_menu=True
pokemon_elegido = None
# Fuente para mostrar el nombre


jugando = True
while jugando:
               
    
    if en_menu:
     for evento in pygame.event.get():
         if evento.type == pygame.QUIT:
            jugando = False
         elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                seleccion = (seleccion - 1) % len(botones)
            elif evento.key == pygame.K_RIGHT:
                seleccion = (seleccion + 1) % len(botones)
            elif evento.key == pygame.K_RETURN:
                pokemon_elegido = botones[seleccion]
                en_menu=False   
        
     ventana.blit(fondo_menu, (0, 0))

    # Dibujar imágenes
     for i, (imagen, x, y) in enumerate(botones):
        ventana.blit(imagen, (x, y))
        if i == seleccion:
            # Dibujar un borde rojo para indicar selección
            pygame.draw.rect(ventana, ROJO, (x-5, y-5, imagen.get_width()+10, imagen.get_height()+10), 3)

    # Mostrar nombre del Pokémon seleccionado
     nombres = ["Charmander", "Squirtle", "Bulbasaur"]
     texto = fuente.render(nombres[seleccion], True, ROJO)
     ventana.blit(texto, (ANCHO//2 - texto.get_width()//2, 50))
    
    else: 
       
            
        seleccion1=4
        if seleccion1==4:seleccion1=seleccion
        ventana.blit(fondo_juego, (0, 0))
        if seleccion1==0: 
            ventana.blit(charmander_img, (80,100))
            for i in range(6):  
             texto=fuente.render(f"{pokemon.stats[i]}{pokemon.stats1[i]}",True,ROJO)
             ventana.blit(texto, (400,450+i*30))
        elif seleccion1==1:
            ventana.blit(squirtle_img, (80,180))
            for i in range(6):  
             texto=fuente.render(f"{pokemon.stats[i]}{pokemon.stats2[i]}",True,ROJO)
             ventana.blit(texto, (400,450+i*30))
        elif seleccion1==2: 
            ventana.blit(bulbasaur_img, (80, 180))
            for i in range(6):  
             texto=fuente.render(f"{pokemon.stats[i]}{pokemon.stats3[i]}",True,ROJO)
             ventana.blit(texto, (400,450+i*30))
            
        
     
     

    pygame.display.update()

pygame.quit()
