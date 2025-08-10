import pygame

# Inicializar pygame
pygame.init()

# Configuración de ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pokémon - Elección Inicial")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Cargar fondos
fondo_menu = pygame.image.load("fondo_inicial.png").convert()
fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO, ALTO))

fondo_juego = pygame.image.load("fondo2.png").convert()
fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO, ALTO))

# Cargar Pokémon
pokemons = [
    {"nombre": "Bulbasaur", "img": pygame.image.load("bulbasaur.png")},
    {"nombre": "Charmander", "img": pygame.image.load("charmander.png")},
    {"nombre": "Squirtle", "img": pygame.image.load("squirtle.png")}
]

# Escalar imágenes de Pokémon
for p in pokemons:
    p["img"] = pygame.transform.scale(p["img"], (150, 150))

# Fuente
fuente = pygame.font.SysFont("Arial", 30, bold=True)

# Variables de estado
seleccion = 0  # 0 = Bulbasaur, 1 = Charmander, 2 = Squirtle
en_menu = True
pokemon_elegido = None

# Bucle principal
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        if en_menu:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    seleccion = (seleccion - 1) % 3
                if evento.key == pygame.K_RIGHT:
                    seleccion = (seleccion + 1) % 3
                if evento.key == pygame.K_RETURN:
                    pokemon_elegido = pokemons[seleccion]
                    en_menu = False

    if en_menu:
        # Dibujar fondo
        ventana.blit(fondo_menu, (0, 0))

        # Dibujar opciones de Pokémon
        for i, p in enumerate(pokemons):
            x = 150 + i * 250
            y = 300
            ventana.blit(p["img"], (x, y))

            # Texto debajo
            texto = fuente.render(p["nombre"], True, NEGRO)
            ventana.blit(texto, (x + 20, y + 160))

            # Resaltar selección
            if i == seleccion:
                pygame.draw.rect(ventana, NEGRO, (x - 5, y - 5, 160, 200), 3)

        # Instrucciones
        instr = fuente.render("Usa ← → para elegir, ENTER para seleccionar", True, NEGRO)
        ventana.blit(instr, (ANCHO//2 - instr.get_width()//2, 100))

    else:
        # Pantalla del juego con el Pokémon elegido
        ventana.blit(fondo_juego, (0, 0))
        ventana.blit(pokemon_elegido["img"], (ANCHO//2 - 75, ALTO//2 - 75))

        texto = fuente.render(f"Tu Pokémon inicial es {pokemon_elegido['nombre']}!", True, BLANCO)
        ventana.blit(texto, (ANCHO//2 - texto.get_width()//2, 50))

    pygame.display.update()

pygame.quit()
