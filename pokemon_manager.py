from pokemon_base import *
from random import randint

def construir_pokemon_agua(vida=44, ataque=48, defensa=65):
    return PokemonAgua(ataque, defensa, vida)

def construir_pokemon_fuego(vida=39, ataque=52, defensa=43):
    return PokemonFuego(ataque, defensa, vida)

def construir_pokemon_electrico(vida=20, ataque=40, defensa=15):
    return PokemonElectrico(ataque, defensa, vida)

def construir_pokemon_hierba(vida=45, ataque=49, defensa=49):
    return PokemonHierba(ataque, defensa, vida)

def construir_pokemon_random(vida=10, ataque=10, defensa=10):
    tipo = randint(1, 4)
    if tipo == 1:
        return PokemonAgua(ataque, defensa, vida)
    elif tipo == 2:
        return PokemonFuego(ataque, defensa, vida)
    elif tipo == 3:
        return PokemonElectrico(ataque, defensa, vida)
    elif tipo == 4:
        return PokemonHierba(ataque, defensa, vida)
    
    return None

def crearPokemonInicial(tipo):
    if tipo == 1:
        return construir_pokemon_fuego()
    elif tipo == 2:
        return construir_pokemon_hierba()
    elif tipo == 3:
        return construir_pokemon_agua()
    else:
        return construir_pokemon_electrico()