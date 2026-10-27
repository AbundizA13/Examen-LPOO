from random import randint
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
pokemon.detallesPokemon()
print("Diviértete en esta aventura\n")

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
        pokemon.detallesPokemon()
        print("\n")
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
                print("\n")
            elif opci==3:
                pass
            elif opci==4:
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
                elif opcio==2:
                    print("\n-------Entrenamiento Individual--------")
                    print("1. Incrementar Ataque")
                    print("2. Incrementar Defensa")
                    print("3. Incrementar Vida")
                    print("0. Salir")
                    print("---------------------")
                    opcion= int(input("Ingrese una opción: "))
                    if opcion==1:
                        print("\n-------Incrementar Ataque--------")
                        pokemon.incrementar_ataque()
                        print(f"{pokemon} Incrementó su ataque +10")
                    elif opcion==2:
                        print("\n-------Incrementar Defensa--------")
                        pokemon.incrementar_defensa()
                        print(f"{pokemon} Incrementó su defensa +10")
                    elif opcion==3:
                        print("\n-------Incrementar Vida--------")
                        pokemon.incrementar_vida()
                        print(f"{pokemon.nombre} Incrementó su vida +10")
                        pokemon.incrementar_vida()
                    elif opcion==0:
                        break
                    else:
                        print("Ingrese una opción correcta")
                elif opcio==3:
                    #FALTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                    pass
                elif opcio==4:
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
                    elif opcion==2:
                        print("\n-------Incrementar Defensa--------")
                        increment= int(input("Ingrese el incremento del ataque: "))
                        pokemon.subir_defensa(increment)
                        print(f"{pokemon.nombre} Incrementó su defensa +{increment}")
                    elif opcion==3:
                        print("\n-------Incrementar Vida--------")
                        incremento= int(input("Ingrese el incremento del ataque: "))
                        pokemon.subir_vida(incremento)
                        print(f"{pokemon.nombre} Incrementó su vida +{incremento}")
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
    elif opc==3:
        #FALTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        pass
    elif opc==4:
        pass
    elif opc==5:
        pass
    elif opc==0:
        break
    else:
        print("Ingrese una opción correcta")
