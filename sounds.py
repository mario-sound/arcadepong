import pygame

pygame.mixer.init()

sonido_rebote = pygame.mixer.Sound("/Users/mariosanchezmolina/Documents/ConquerBlocks/Python/_Proyectos/Tools/arcadepong/sounds/rebote.ogg")
sonido_punto = pygame.mixer.Sound("/Users/mariosanchezmolina/Documents/ConquerBlocks/Python/_Proyectos/Tools/arcadepong/sounds/punto.ogg")
sonido_marcador = pygame.mixer.Sound("/Users/mariosanchezmolina/Documents/ConquerBlocks/Python/_Proyectos/Tools/arcadepong/sounds/marcador.ogg")
sonido_pared = pygame.mixer.Sound("/Users/mariosanchezmolina/Documents/ConquerBlocks/Python/_Proyectos/Tools/arcadepong/sounds/pared.ogg")
sonido_mover_paleta = pygame.mixer.Sound("/Users/mariosanchezmolina/Documents/ConquerBlocks/Python/_Proyectos/Tools/arcadepong/sounds/mover_paleta.ogg")

def reproducir_sonido_rebote():
    sonido_rebote.play()

def reproducir_sonido_punto():
    sonido_punto.play()

def reproducir_sonido_marcador():
    sonido_marcador.play()

def reproducir_sonido_pared():
    sonido_pared.play()

def reproducir_sonido_mover_paleta():
    sonido_mover_paleta.play()