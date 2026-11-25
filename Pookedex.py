from combate import Combate
from pokemon_manager import *
from copy import deepcopy
from Persistencia import *
import msvcrt

import os

def Limpiar():
    os.system("cls")

def Elegir_Pokemon(nombre:str):
    Limpiar()
    print("\t\t-------Pookédex--------")
    print("Bienvenido a tu aventura Pokemon viendo temas de POO")
    print(f"\nMuy bien, {nombre}, aún no tienes ningún Pokémon.")
    print("Debes elegir uno de los 4 que tenemos para ti:")

    print("1. Charmander (Fuego)")
    print("2. Bulbasaur (Hierba)")
    print("3. Squirtle (Agua)")
    print("4. Pichu (Eléctrico)")
    print("0. Al azar")
    print("---------------------")

    while True:
        try: 
            opcion = int(input("Ingrese una opción: "))
            if opcion >= 0 and opcion <=4:
                opcion = int(opcion)
                break
            else:
                print("Pokemon no valido...")
        except ValueError:
            print("Error: No puedes dejarlo vacío ni escribir letras. Ingresa un número.")

    if opcion == 0:
        opcion = randint(1, 4)

    pokemon = crearPokemonInicial(opcion)
    print(f"\nExcelente {nombre}. Tu acompañante es {pokemon.get_nombre()}")
    pokemon.detalles_pokemon()
    print("Diviértete en esta aventura\n")
    enter_para_continuar()
    Limpiar()
    return pokemon

def opcion_1(pokemon):
    print("\n-------Detalles--------")
    pokemon.detalles_pokemon()
    enter_para_continuar()
    Limpiar()

def opcion_2(pokemon:Pokemon):
    while True:
        try:
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
                pokemon.solucionar_evolucion()
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
        except ValueError:
            print("Error: No puedes dejarlo vacío ni escribir letras. Ingresa un número.")


def opcion_3(pokemon, enemigos, capturados, partida):  # partida: para saber a qué partida pertenece el log
    tamano_enemigos = len(enemigos)
    if tamano_enemigos == 0:
        print("Debes crear enemigos antes de combatir.")
        enter_para_continuar()
        Limpiar()
        return
    random = randint(0, tamano_enemigos - 1)
    enemigo_actual = enemigos[random]
    enemigo_pelear = deepcopy(enemigo_actual)
    combate = Combate(pokemon, enemigo_pelear)
    estado_combate = combate.ciclo_combate()
    if estado_combate == "VICTORIA":  # ciclo_combate ahora regresa "VICTORIA", "DERROTA" o "HUIDA"
        enemigo_actual.set_atrapado()
        capturados.append(enemigo_actual)
    #Esto lo puedes usar para escribirlo directamente en el .txt, con algunos retoques
    combate.get_log() #THIAGO
    enter_para_continuar()
    Limpiar()



def opcion_4(pokemon, capturados):
    print("Pokemons capturados: ")
    for capturado in capturados:
        capturado.detalles_pokemon()
    enter_para_continuar()
    Limpiar()

def opcion_5(pokemon, enemigos):
    try:
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

        if tipo == 5:
            print("Enemigos almacenados:\n+---------------+")
            for enemigo in enemigos:
                enemigo.detalles_pokemon()
                print("+---------------+")
            enter_para_continuar()
            Limpiar()
            return

        try:
            ataque = int(input("Ingresa el ataque (1-1000): "))
            defensa = int(input("Ingresa la defensa (1-1000): "))
            vida = int(input("Ingresa la vida (1-1000): "))

            if not (1 <= ataque <= 1000 and 1 <= defensa <= 1000 and 1 <= vida <= 1000):
                raise ValueError("Error: Todos los valores deben estar en el rango 1-1000.")

            if tipo == 1:
                enemigo = construir_pokemon_fuego(vida=vida, ataque=ataque, defensa=defensa)
            elif tipo == 2:
                enemigo = construir_pokemon_hierba(vida=vida, ataque=ataque, defensa=defensa)
            elif tipo == 3:
                enemigo = construir_pokemon_agua(vida=vida, ataque=ataque, defensa=defensa)
            elif tipo == 4:
                enemigo = construir_pokemon_electrico(vida=vida, ataque=ataque, defensa=defensa)
        
        except ValueError as error:
            print(error)

        enemigos.append(enemigo)
        print(f"\n{enemigo.get_nombre()} se agregó a la lista de enemigos")
        enemigo.detalles_pokemon()
    
    except ValueError:
        print("Error: No puedes dejarlo vacío ni escribir letras. Ingresa un número.")

    enter_para_continuar()
    Limpiar()

def opcion_entrenamiento(pokemon):
    while True:
        try:
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
        except ValueError:
            print("Error: Debe Ingresar numeros enteros!")

def Entrenamiento_normal(pokemon):
    print("\n-------Entrenamiento Normal--------")
    pokemon.entrenar()
    pokemon.detalles_pokemon()

def Entrenamiento_individual(pokemon):
    while True:
        try:
            print("\n-------Entrenamiento Individual--------")
            print("1. Incrementar Ataque")
            print("2. Incrementar Defensa")
            print("3. Incrementar Vida")
            print("0. Salir")
            print("---------------------")
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                print("\n-------Incrementar Ataque--------")
                pokemon.subir_ataque(20)
                print(f"{pokemon.get_nombre()} Incrementó su ataque +20")
                pokemon.detalles_pokemon()
            elif opcion == 2:
                print("\n-------Incrementar Defensa--------")
                pokemon.subir_defensa(20)
                print(f"{pokemon.get_nombre()} Incrementó su defensa +20")
                pokemon.detalles_pokemon()
            elif opcion == 3:
                print("\n-------Incrementar Vida--------")
                pokemon.subir_vida(20)
                print(f"{pokemon.get_nombre()} Incrementó su vida +20")
                pokemon.detalles_pokemon()
            elif opcion == 0:
                break
            else:
                print("Ingrese una opción correcta")
        except ValueError:
            print("Error: Debes ingresar valores enteros, no dejar campos vacios!")
        

def Entrenamiento_Intensivo(pokemon):
    pokemon.actualizar(20, 20, 20)
    pokemon.subir_nivel(20)
    print(f"El pokemon {pokemon.get_nombre()} ha entrenado... Ataque +20, Vida +20, Defensa +20, Nivel +20")
    pokemon.detalles_pokemon()

def Entrenamiento_Personalizado(pokemon):
    while True:
        try:    
            print("\n-------Entrenamiento Personalizado--------")
            print("1. Incrementar Ataque")
            print("2. Incrementar Defensa")
            print("3. Incrementar Vida")
            print("0. Salir")
            print("-------------------------------------------")
            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                Limpiar()
                try:
                    print("\n------- Incrementar Ataque --------")
                    incremento = int(input("Ingrese el incremento del ataque: "))

                    if incremento < 0:
                        raise ValueError("No puedes bajarte el ataque")

                    pokemon.subir_ataque(incremento)
                    print(f"{pokemon.get_nombre()} Incrementó su ataque +{incremento}")
                    pokemon.detalles_pokemon()
                
                except ValueError:
                    print("Error: Solo puedes ingresar valores enteros sin campos vacios!")   

                except ValueError as error:
                    print(f"Error: {error}")
                
                enter_para_continuar()
                Limpiar()

            elif opcion == 2:
                Limpiar()
                try:
                    print("\n-------Incrementar Defensa--------")
                    incremento = int(input("Ingrese el incremento de la defensa: "))
                    
                    if incremento < 0:
                        raise ValueError("No puedes Bajarle la defensa")

                    pokemon.subir_defensa(incremento)
                    print(f"{pokemon.get_nombre()} Incrementó su defensa +{incremento}")
                    pokemon.detalles_pokemon()
                except ValueError:
                    print("Error: Solo puedes ingresar valores enteros sin campos vacios!")

                except ValueError as error:
                    print(f"Error: {error}")

                enter_para_continuar()
                Limpiar()

            elif opcion == 3:
                Limpiar()
                try:    
                    print("\n-------Incrementar Vida--------")
                    incremento = int(input("Ingrese el incremento de la vida: "))

                    if incremento < 0:
                        raise ValueError("No puedes Bajarle la vida")

                    pokemon.subir_vida(incremento)
                    print(f"{pokemon.get_nombre()} Incrementó su vida +{incremento}")
                    pokemon.detalles_pokemon()
                except ValueError:
                    print("Error: Debes ingresar unicamente valores enteros sin dejar campos vacios.")

                except ValueError as error:
                    print(f"Error: {error}")

                enter_para_continuar()
                Limpiar()

            elif opcion == 0:
                break
            else:
                print("Ingrese una opción correcta")
        except ValueError:
            print("Error: Debe ingresar unicamente valores enteros!")

def guardar_partida(bd, partida):
    bd.guardar_partida(partida)
    print("Partida guardada.")

def Main(bd, partida):
    pokemon = partida.get_pkm_principal()
    enemigos = partida.get_pkm_creados()
    capturados = partida.get_pkm_capturados()

    while True:
        try: 
            print(f"\n¿Qué deseas hacer, {partida.get_nombre()}?")
            print("-+--------Menú---------+-")
            print("1. Detalles de mi pokemon")
            print("2. Interacciones Pokemon")
            print("3. Combatir")
            print("4. Ver Pokémon atrapados")
            print("5. Crear Pokémon enemigo")
            print("6. Guardar partida.")
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
                opcion_3(pokemon, enemigos, capturados, partida)
            elif opcion == 4:
                Limpiar()
                opcion_4(pokemon, capturados)
            elif opcion == 5:
                Limpiar()
                opcion_5(pokemon, enemigos)
            elif opcion == 6:
                Limpiar()
                guardar_partida(bd, partida)
                enter_para_continuar()
            elif opcion == 0:
                guardar_partida(bd, partida)
                break
            else:
                print("Opcion no valida...")
                enter_para_continuar()
                Limpiar()
        except ValueError:
            print("Error: Para ingresar opciones, ingrese solo \nnumeros enteros sin dejar campos vacios")

def enter_para_continuar():
    print("\nPresiona ENTER para continuar...", end="", flush=True)
    while True:
        tecla = msvcrt.getch()
        if tecla == b'\r':  # b'\r' es el código de la tecla ENTER en Windows
            print()  # Hace el salto de línea normal al presionar Enter
            break

def elegir_partida(base_datos:BaseDatos):
    while True:
        try:
            for estado_partida in base_datos.obtener_output_menu_partidas():
                print(estado_partida)
            id_partida = int(input("Dame el número de slot de partida a usar: "))
            if id_partida not in (1,2,3):
                raise ValueError("El slot debe ser 1, 2 o 3.")
            partida_cargada = base_datos.obtener_partida(id_partida)

            if partida_cargada is None:
                partida_cargada = crear_partida_vacia(id_partida)
            return partida_cargada
        except ValueError as e:
            print(f"Entrada inválida: {e}")
            enter_para_continuar()
            Limpiar()

def crear_partida_vacia(id_partida:int):
    while True:
        try:
            nombre = str(input("Dame el nombre tu nombre para esta partida: "))
            break
        except ValueError:
            print("Error: Debe ingresar el nombre en string sin dejar campo vacio.")
        
    return Partida(id_partida, nombre)


bd = BaseDatos()
bd.iniciar()

partida = elegir_partida(bd)

if partida.get_pkm_principal() is None:
    pokemon_predeterminado = Elegir_Pokemon(partida.get_nombre())
    partida.set_pkm_principal(pokemon_predeterminado)
#Main(pokemon_predeterminado, partida.get_pkm_creados(), partida.get_pkm_capturados())
Main(bd, partida)
bd.guardar_partida(partida)