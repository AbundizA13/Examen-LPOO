from random import randint
from random import choice
from pokemon_manager import *

print("-------Pookédex--------")
print("Bienvenido a tu aventura Pokemon viendo temas de POO")
nombre = input("Antes de empezar, ¿cuál es tu nombre?: ")

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
    cho= int(input("Ingrese una opción: "))
    if cho >= 0 and cho <=4:
        cho= int(cho)
        break
    else:
        print("La opción no parece correcta, intente de nuevo.")

if cho == 0:
    cho = randint(1, 4)

pokemon = crearPokemonInicial(cho)
print(f"\nExcelente {nombre}. Tu acompañante es {pokemon.nombre}")
pokemon.detalles_pokemon()
print("Diviértete en esta aventura\n")

enemigos = []
pokemones_atrapados = []

while True:
    print("\n-------Menú--------")
    print("1. Detalles de mi pokemon")
    print("2. Interacciones Pokemon")
    print("3. Combatir")
    print("4. Ver Pokémon atrapados")
    print("5. Crear Pokémon enemigo")
    print("0. Salir")
    print("---------------------")
    opc= int(input("Ingrese una opción: "))

    if opc==1:
        ''''
        Muestra en pantalla todos los detalles del Pokémon (nombre, descripción, ataque, defensa, vida,
        nivel, evolución, y si ha sido atrapado).
        '''
        print("\n-------Detalles--------")
        pokemon.detalles_pokemon()
    elif opc==2:
        while True:
            print("\n-------Interacciones--------")
            print("1. Jugar")
            print("2. Hablar")
            print("3. Alimentar")
            print("4. Entrenamiento")
            print("0. Salir")
            print("---------------------")
            opci= int(input("Ingrese una opción: "))
            if opci==1:
                pass
            elif opci==2:
                pokemon.hablar()
            elif opci==3:
                pass
            elif opci==4:
                while True:
                    print("\n-------Entrenamiento--------")
                    print("1. Entrenamiento Normal")
                    print("2. Entrenamiento Individual")
                    print("3. Entrenamiento Intensivo")
                    print("4. Entrenamiento Personalizado")
                    print("0. Salir")
                    print("---------------------")
                    opcio= int(input("Ingrese una opción: "))
                    if opcio==1:
                        print("\n-------Entrenamiento Normal--------")
                        pokemon.entrenar()
                        pokemon.detalles_pokemon()
                    elif opcio==2:
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
                                print(f"{pokemon.nombre} Incrementó su ataque +20")
                                pokemon.detalles_pokemon()
                            elif opcion==2:
                                print("\n-------Incrementar Defensa--------")
                                pokemon.subir_defensa(20)
                                print(f"{pokemon.nombre} Incrementó su defensa +20")
                                pokemon.detalles_pokemon()
                            elif opcion==3:
                                print("\n-------Incrementar Vida--------")
                                pokemon.subir_vida(20)
                                print(f"{pokemon.nombre} Incrementó su vida +20")
                                pokemon.detalles_pokemon()
                            elif opcion==0:
                                break
                            else:
                                print("Ingrese una opción correcta")
                    elif opcio==3:
                        pokemon.actualizar(20,20,20)
                        print(f"El pokemon {pokemon.nombre} ha entrenado... Ataque +20, Vida +20, Defensa +20")
                        pokemon.detalles_pokemon()
                    elif opcio==4:
                        while True:
                            print("\n-------Entrenamiento Personalizado--------")
                            print("1. Incrementar Ataque")
                            print("2. Incrementar Defensa")
                            print("3. Incrementar Vida")
                            print("0. Salir")
                            print("---------------------")
                            opcion= int(input("Ingrese una opción: "))
                            if opcion==1:
                                print("\n-------Incrementar Ataque--------")
                                incremen= int(input("Ingrese el incremento del ataque: "))
                                pokemon.subir_ataque(incremen)
                                print(f"{pokemon.nombre} Incrementó su ataque +{incremen}")
                                pokemon.detalles_pokemon()
                            elif opcion==2:
                                print("\n-------Incrementar Defensa--------")
                                increment= int(input("Ingrese el incremento de la defensa: "))
                                pokemon.subir_defensa(increment)
                                print(f"{pokemon.nombre} Incrementó su defensa +{increment}")
                                pokemon.detalles_pokemon()
                            elif opcion==3:
                                print("\n-------Incrementar Vida--------")
                                incremento= int(input("Ingrese el incremento de la vida: "))
                                pokemon.subir_vida(incremento)
                                print(f"{pokemon.nombre} Incrementó su vida +{incremento}")
                                pokemon.detalles_pokemon()
                            elif opcion==0:
                                break
                            else:
                                print("Ingrese una opción correcta")
                    elif opcio==0:
                        break
                    else:
                        print("Ingrese una opción correcta")
            elif opci==0:
                break
            else:
                print("Ingrese una opción correcta")

# Falta terminar la opcion 3 y definir que se gane al enemigo en la opcion 4
    elif opc==3:
        while True:
            enemigo = choice(enemigos)
            print("\n-------Combate--------")
            print("1. Pasar Turno")
            print("2. Ataque Normal")
            print("3. Ataque Especial")
            print("4. Huir")
            op= int(input("Ingrese una opción: "))

            if op==1:
                ataques_al_enemigo(pokemon, enemigo)
                
            elif op==2:
                ataques_al_enemigo(pokemon, enemigo)    

            elif op==3:
                ataques_al_enemigo(pokemon, enemigo)
                
            elif op==4:
                break
    elif opc==4:
        print("------- Pokemones Atrapados -------")
        for pokemon in pokemones_atrapados:
            print(pokemon)

        #FALTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        pass
    elif opc==5:
        print("\n-------Creación--------")
        print("1. Fuego")
        print("2. Hierba")
        print("3. Agua")
        print("4. Eléctrico")
        print("0. Cancelar")
        print("---------------------")
        tipo= int(input("Ingrese el tipo del Pokémon: "))
        if tipo==0:
            continue
        if tipo < 1 or tipo > 4:
            print("Ingrese una opción correcta")
            continue
        ataque= int(input("Ingresa el ataque (1-1000): "))
        defensa= int(input("Ingresa la defensa (1-1000): "))
        vida= int(input("Ingresa la vida (1-1000): "))

        if tipo == 1:
            enemigo = construir_pokemon_fuego(vida=vida, ataque=ataque, defensa=defensa)
        elif tipo == 2:
            enemigo = construir_pokemon_hierba(vida=vida, ataque=ataque, defensa=defensa)
        elif tipo == 3:
            enemigo = construir_pokemon_agua(vida=vida, ataque=ataque, defensa=defensa)
        else:
            enemigo = construir_pokemon_electrico(vida=vida, ataque=ataque, defensa=defensa)
        enemigos.append(enemigo)
        print(f"\n{enemigo.nombre} se agregó a la lista de enemigos")
        enemigo.detalles_pokemon()
        
    elif opc==0:
        break
    else:
        print("Ingrese una opción correcta")