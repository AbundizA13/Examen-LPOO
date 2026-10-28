from combate import Combate
from pokemon_manager import *
from copy import deepcopy

import os

def Limpiar():
    os.system("cls")

# Crea el objeto pokemon
def Elegir_Pokemon():
    print("-------Pookédex--------")
    print("Bienvenido a tu aventura Pokemon viendo temas de POO")
    nombre = input("Antes de empezar, ¿cuál es tu nombre?: ")

    Limpiar()

    print(f"\nMuy bien, {nombre}, aún no tienes ningún Pokémon.")
    print("Debes elegir uno de los 4 que tenemos para ti:")

    #Este es el punto donde se elige uno de los 4 pokemones cuando estamos en nuestra aventura
    print("1. Charmander (Fuego)")
    print("2. Bulbasaur (Hierba)")
    print("3. Squirtle (Agua)")
    print("4. Pichu (Eléctrico)")
    print("0. Al azar")
    print("---------------------")

    while True:
        opcion = int(input("Ingrese una opción: "))
        if opcion >= 0 and opcion <=4:
            opcion = int(opcion)
            break
        else:
            print("Pokemon no valido...")

    if opcion == 0:
        opcion = randint(1, 4)

    pokemon = crearPokemonInicial(opcion)
    print(f"\nExcelente {nombre}. Tu acompañante es {pokemon.get_nombre()}")
    pokemon.detalles_pokemon()
    print("Diviértete en esta aventura\n")
    enter_para_continuar()
    Limpiar()

    return pokemon

# CLASE OPCIONES - MAIN
# Opcion 1 -> 1 - Detalles de pokemon
def opcion_1(pokemon):
    ''''
    Muestra en pantalla todos los detalles del Pokémon (nombre, descripción, ataque, defensa, vida,
    nivel, evolución, y si ha sido atrapado).
    '''
    print("\n-------Detalles--------")
    pokemon.detalles_pokemon()
    enter_para_continuar()
    Limpiar()

# Opcion 1 -> 2 - Interacciones de pokemon
def opcion_2(pokemon:Pokemon):
    while True:
        print("\n-------Interacciones--------")
        print("1. Jugar")
        print("2. Hablar")
        print("3. Alimentar")
        print("4. Entrenamiento")
        print("0. Salir")
        print("---------------------")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            print(f"Has jugado con {pokemon.get_nombre()}")
            enter_para_continuar()
            Limpiar()

        elif opcion == 2:
            pokemon.hablar()
            enter_para_continuar()
            Limpiar()

        elif opcion == 3:
            niveles_agregados = randint(2,4)
            print(f"Has alimentado a {pokemon.get_nombre()}.\nSu nivel ha incrementado +{niveles_agregados}")
            pokemon.subir_nivel(niveles_agregados)
            enter_para_continuar()
            Limpiar()

        elif opcion == 4:
            opcion_entrenamiento(pokemon)
            enter_para_continuar()
            Limpiar()
        elif opcion == 0:
            print("Saliendo...")
            enter_para_continuar()
            Limpiar()
            break
        else:
            print("Ingrese una opción correcta...")
            enter_para_continuar()
            Limpiar()

# Opcion 1 -> 3 - Combate
def opcion_3(pokemon, enemigos, capturados):
    tamano_enemigos = len(enemigos)
    if tamano_enemigos == 0:
        print("Debes crear enemigos antes de combatir.")
        enter_para_continuar()
        Limpiar()
        return
    random = randint(0,tamano_enemigos-1)
    enemigo_actual = enemigos[random]
    enemigo_pelear = deepcopy(enemigo_actual)
    combate = Combate(pokemon, enemigo_pelear)
    estado_combate = combate.ciclo_combate()
    if estado_combate:
        enemigo_actual.set_atrapado()
        capturados.append(enemigo_actual)
    enter_para_continuar()
    Limpiar()



# Opcion 1 -> 4 - Pokemon Atrapado
def opcion_4(pokemon, capturados):
    print("Pokemons capturados: ")
    for capturado in capturados:
        capturado.detalles_pokemon()
    enter_para_continuar()
    Limpiar()

# Opcion 1 -> 5 - Crear Pokemon enemigo 
def opcion_5(pokemon, enemigos):
    print("\n-------Creación--------")
    print("1. Fuego.")
    print("2. Hierba.")
    print("3. Agua.")
    print("4. Eléctrico.")
    print("5. Ver enemigos almacenados.")
    print("0. Cancelar.")
    print("---------------------")
    tipo = int(input("Ingrese el tipo del Pokémon: "))
    
    if tipo == 0:
        print("Cancelando...")
        return 

    if tipo < 1 or tipo > 5:
        print("Ingrese una opción correcta")
        return

    ataque = int(input("Ingresa el ataque (1-1000): "))
    defensa = int(input("Ingresa la defensa (1-1000): "))
    vida = int(input("Ingresa la vida (1-1000): "))

    if tipo == 1:
        enemigo = construir_pokemon_fuego(vida=vida, ataque=ataque, defensa=defensa)
    elif tipo == 2:
        enemigo = construir_pokemon_hierba(vida=vida, ataque=ataque, defensa=defensa)
    elif tipo == 3:
        enemigo = construir_pokemon_agua(vida=vida, ataque=ataque, defensa=defensa)
    elif tipo == 4:
        enemigo = construir_pokemon_electrico(vida=vida, ataque=ataque, defensa=defensa)
    else:
        print("Enemigos almacenados:\n+---------------+")
        for enemigo in enemigos:
            enemigo.detalles_pokemon()
            print("+---------------+")
            enter_para_continuar()
            Limpiar()
        return

    enemigos.append(enemigo)
    print(f"\n{enemigo.get_nombre()} se agregó a la lista de enemigos")
    enemigo.detalles_pokemon()
    enter_para_continuar()
    Limpiar()

# Opcion de entrenamiento
def opcion_entrenamiento(pokemon):
    while True:
        print("\n-------Entrenamiento--------")
        print("1. Entrenamiento Normal")
        print("2. Entrenamiento Individual")
        print("3. Entrenamiento Intensivo")
        print("4. Entrenamiento Personalizado")
        print("0. Salir")
        print("------------------------------")
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            Entrenamiento_normal(pokemon)
            enter_para_continuar()
            Limpiar()
        elif opcion == 2:
            Entrenamiento_individual(pokemon)
            enter_para_continuar()
            Limpiar()
        elif opcion == 3:
            Entrenamiento_Intensivo(pokemon)
            enter_para_continuar()
            Limpiar()
        elif opcion == 4:
            Entrenamiento_Personalizado(pokemon)
            enter_para_continuar()
            Limpiar()
        elif opcion == 0:
            break
        else:
            print("Ingrese una opción correcta")
            enter_para_continuar()
            Limpiar()

# CLASE ENTRENAMIENTO
# Opciones de entrenamiento
def Entrenamiento_normal(pokemon):
    print("\n-------Entrenamiento Normal--------")
    pokemon.entrenar()
    pokemon.detalles_pokemon()

# Entrenamiento individual
def Entrenamiento_individual(pokemon):
    while True:
        print("\n-------Entrenamiento Individual--------")
        print("1. Incrementar Ataque")
        print("2. Incrementar Defensa")
        print("3. Incrementar Vida")
        print("0. Salir")
        print("---------------------")
        opcion= int(input("Ingrese una opción: "))
        if opcion==1:
            print("\n-------Incrementar Ataque--------")
            pokemon.subir_ataque(20)
            print(f"{pokemon.get_nombre()} Incrementó su ataque +20")
            pokemon.detalles_pokemon()
        elif opcion==2:
            print("\n-------Incrementar Defensa--------")
            pokemon.subir_defensa(20)
            print(f"{pokemon.get_nombre()} Incrementó su defensa +20")
            pokemon.detalles_pokemon()
        elif opcion==3:
            print("\n-------Incrementar Vida--------")
            pokemon.subir_vida(20)
            print(f"{pokemon.get_nombre()} Incrementó su vida +20")
            pokemon.detalles_pokemon()
        elif opcion==0:
            break
        else:
            print("Ingrese una opción correcta")

# Entrenamiento Intensivo
def Entrenamiento_Intensivo(pokemon):
    pokemon.actualizar(20, 20, 20)
    pokemon.subir_nivel(20)
    print(f"El pokemon {pokemon.get_nombre()} ha entrenado... Ataque +20, Vida +20, Defensa +20, Nivel +20")
    pokemon.detalles_pokemon()

# Entrenamiento Personalizado
def Entrenamiento_Personalizado(pokemon):
    while True:
        print("\n-------Entrenamiento Personalizado--------")
        print("1. Incrementar Ataque")
        print("2. Incrementar Defensa")
        print("3. Incrementar Vida")
        print("0. Salir")
        print("---------------------")
        opcion= int(input("Ingrese una opción: "))
        
        if opcion == 1:
            Limpiar()
            print("\n-------Incrementar Ataque--------")
            incremen= int(input("Ingrese el incremento del ataque: "))
            pokemon.subir_ataque(incremen)
            print(f"{pokemon.get_nombre()} Incrementó su ataque +{incremen}")
            pokemon.detalles_pokemon()
            enter_para_continuar()
            Limpiar()
        
        elif opcion == 2:
            Limpiar()
            print("\n-------Incrementar Defensa--------")
            increment= int(input("Ingrese el incremento de la defensa: "))
            pokemon.subir_defensa(increment)
            print(f"{pokemon.get_nombre()} Incrementó su defensa +{increment}")
            pokemon.detalles_pokemon()
            enter_para_continuar()
            Limpiar()

        elif opcion == 3:
            Limpiar(0)
            print("\n-------Incrementar Vida--------")
            incremento= int(input("Ingrese el incremento de la vida: "))
            pokemon.subir_vida(incremento)
            print(f"{pokemon.get_nombre()} Incrementó su vida +{incremento}")
            pokemon.detalles_pokemon()
            enter_para_continuar()
            Limpiar()

        elif opcion == 0:
            break
        else:
            print("Ingrese una opción correcta")

# Lleva un arreglo de funciones
# internas
def Main(pokemon, enemigos, capturados):
    while True:
        print("\n-------Menú--------")
        print("1. Detalles de mi pokemon")
        print("2. Interacciones Pokemon")
        print("3. Combatir")
        print("4. Ver Pokémon atrapados")
        print("5. Crear Pokémon enemigo")
        print("0. Salir")
        print("---------------------")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            Limpiar()
            opcion_1(pokemon)
        elif opcion == 2:
            Limpiar()
            opcion_2(pokemon)
        elif opcion == 3:
            Limpiar()
            opcion_3(pokemon, enemigos, capturados)
        elif opcion == 4:
            Limpiar()
            opcion_4(pokemon, capturados)
        elif opcion == 5:
            Limpiar()
            opcion_5(pokemon, enemigos)
        elif opcion == 0:
            break
        else:
            print("Opcion no valida...")
            enter_para_continuar()
            Limpiar()

def enter_para_continuar():
    input("\nENTER para continuar.\n")

# Ejemplo de uso:
# Pokemon_elegido = Elegir_Pokemon()

# Primer Menu (Crear pokemon)
# Devuelve la instancia del pokemon con la que se maneja
enemigos = []
capturados = []

pokemon_predeterminado = Elegir_Pokemon()
Main(pokemon_predeterminado, enemigos, capturados)