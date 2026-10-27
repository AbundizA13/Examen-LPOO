from pokemon_base import *
from random import randint

def construir_pokemon_agua(vida=44, ataque=48, defensa=65):
    return PokemonAgua(vida, ataque, defensa)

def construir_pokemon_fuego(vida=39, ataque=52, defensa=43):
    return PokemonFuego(vida, ataque, defensa)

def construir_pokemon_electrico(vida=20, ataque=40, defensa=15):
    return PokemonElectrico(vida, ataque, defensa)

def construir_pokemon_hierba(vida=45, ataque=49, defensa=49):
    return PokemonHierba(vida, ataque, defensa)

def construir_pokemon_random(vida=10, ataque=10, defensa=10):
    tipo = randint(1, 4)
    if tipo == 1:
        return PokemonAgua(ataque, defensa, vida)
    elif tipo == 2:
        return PokemonFuego(vida, ataque, defensa)
    elif tipo == 3:
        return PokemonElectrico(vida, ataque, defensa)
    elif tipo == 4:
        return PokemonHierba(vida, ataque, defensa)   
    return None

# Cambios a partir de 28 - 69
def crear_pokemonInicial(tipo):
    if tipo == 1:
        return construir_pokemon_agua()
    elif tipo == 2:
        return construir_pokemon_fuego()
    elif tipo == 3:
        return construir_pokemon_electrico()
    elif tipo == 4:
        return Pconstruir_pokemon_hierba()

def ataques_al_enemigo(pokemon, enemigo):
    danio = pokemon.ataque
    if danio > pokemon.ataque:
        sobrante = danio - enemigo.defensa
        enemigo.vida -= sobrante
    else:
        enemigo.defensa -= danio

        # El enemigo te ataca
        accion_enemigo = choice([1, 2, 3])
        pokemon_manager.turno_enemigo(accion_enemigo, pokemon)

def turno_enemigo(enemigo, pokemon):
    accion = randint(1, 3)
    
    if accion == 1:
        print(f"{enemigo.nombre} usó ataque normal!")
        dano = enemigo.ataque
    elif accion == 2:
        print(f"{enemigo.nombre} usó {enemigo.ataque_especial}!")
        dano = enemigo.ataque * 1.5
    else:
        print(f"{enemigo.nombre} pasó su turno.")
        return

    if dano > pokemon.defensa:
        sobrante = dano - pokemon.defensa
        pokemon.defensa = 0
        pokemon.vida -= sobrante
    else:
        pokemon.defensa -= dano