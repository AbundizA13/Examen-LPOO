while True:
    print("-------Pokedex-------")
    #Pokemon atrapados imprime la lista de pokemones atrapados junto con sus 4 entrenamientos
    '''
    Ejemplo:
    --------Lista Pokemon----------
    1. Nombre: Bulbasaur
    Descripcion: jnksdjnk
    Categoria: Planta/Veneno
    Nivel: 5
    ataque: 100
    defensa: 250
    vida: 300
    evolucion: 1
    Atrapado: Si
    Entrenamientos:
    1. Látigo cepa:     Ataque fisico de tipo planta con lianas
    2. Polvo veneno:    Provoca estado alterado de envenenamiento
    3. Hoja afilada:    Ataque cortante de tipo planta
    4. Somnifero:       Duerme al rival (ej. Ataque especial)
    -------------------------
    2. Nombre: Pikachu
    Descripcion: iwddjnjwedj
    Categoria: Electrico
    Nivel 7
    ataque: 100
    defensa: 250
    vida: 300
    evolucion: 2
    Atrapado: No
    Entrenamientos:
    1. Impactrueno:     Ataque electrico básico de inicio
    2. Rayo:            Movimiento eléctrico clásico de gran potencia
    3. Trueno:          Potente ataque electrico de gran presición
    4. Electrobola:     Bola de energía eléctrica cuya potencia depende de la velocidad de Pikachu (ej. Ataque especial)
    ----------------------------
    '''
    #Seguido de eso se presenta un menú con las siguientes
    '''
    #1. Hablar pokemon
    #2. Entrenar pokemon
    #3. Ayuda
    #4. Salir
    '''
    print("1. Lista Pokemon")
    print("2. Batalla Pokemon")
    print("3. Ayuda")
    print("3. Salir")
    print("-----------------------------")
    opc= int(input("Ingrese una opción: "))
    if opc==1:
        while True:
            print("-----------Lista Pokemon------------")
            #Aqui va la lista de todos los pokemon
            print("------Que quieres hacer?-----------")
            print("1. Hablar Pokemon")
            print("2. Entrenar Pokemon")
            print("3. Ver pokemon atrapados")
            print("4. Salir")
            print("-----------------------------")
            opci= int(input("Ingrese una opción: "))
            if opci==1:
                pok= int(input("Ingrese el número del pokemon: "))
                #aqui por medio de un metodo se iran bsucando los pokemon para hacerlo hablar (recuerden que usualmente es su nombre)
            elif opci==2:
                poke= int(input("Ingrese el número del pokemon: "))
                #aqui por medio de un metodo se iran bsucando los pokemon para entrenarlo:
                while True:
                    print("------Que quieres entrenar?------")
                    print("1. Subir Ataque")
                    print("2. Subir Defensa")
                    print("3. Subir Vida")
                    print("4. Salir")
                    print("-----------------------------")
                    opci= int(input("Ingrese una opción: "))
                    if opci==1:
                        #Metodo para incrementar su ataque
                        pass
                    elif opci==2:
                        #metodo para incrementar su defensa
                        pass
                    elif opci==3:
                        #metodo para incrementar su vida
                        pass
                    elif opci==4:
                        pass
                    else:
                        print("La opción no parece correcta")
            elif opci==3:
                #aqui va la lista de SOLO los pokemones atrapados
                pass
            elif opci==4:
                pass
            else:
                print("La opción no parece correcta")
    elif opc==2:
        print("---------Batalla Pokemon---------")
        print("Lista de pokemon atrapados")
        #aqui se deberia mostrar la lista de pokemon atrapados
        print("------------------------------------------")
        combate1= int(input("Ingrese el número de tu pokemon combatiente: "))

        print("------------------------------------------")
        print("Lista de pokemon enemigos")
        print("")
    elif opc==3:
        pass
    elif opc==4:
        break
    else:
        print("La opción no parece correcta")