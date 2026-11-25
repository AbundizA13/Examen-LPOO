from pokemon_base import Pokemon
from random import randint
from time import sleep

class Combate:
    __turno = 1
    aliado = None
    enemigo = None    

    def __init__(self, aliado: Pokemon, enemigo: Pokemon, archivo_Historial):
        self.aliado = aliado
        self.enemigo = enemigo
        self.__log = []
        self.__archivo_Historial = archivo_Historial

    def __registrar(self, texto=""):
        print(texto)
        self.__log.append(texto)
        with open(self.__archivo_historial, "a", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")

    def get_log(self):
        return self.__log

    def ciclo_combate(self):

        while self.enemigo.sigue_vivo() and self.aliado.sigue_vivo():
            self.__mostrar_estado_combate()
            if not self.turno_aliado():
                return "HUIDA"  # el jugador escapó
            self.__mostrar_estado_combate()
            if self.enemigo.sigue_vivo():
                self.turno_enemigo()
                sleep(3)
            self.__turno+=1

        
        if self.imprimir_estado_combate():
            self.procesar_final_combate()
            self.aliado.solucionar_evolucion()
            return "VICTORIA"  # ganó y captura al enemigo

        self.aliado.subir_vida(100)
        return "DERROTA"  # el aliado se quedó sin vida

    def __mostrar_estado_combate(self):
        self.__registrar(f"\n================ TURNO {self.__turno} =================")
        self.__registrar(f"  Aliado: {self.aliado.get_nombre()} | HP: {self.aliado.get_vida()} | DEF: {self.aliado.get_defensa()} |")
        self.__registrar(f"  Enemigo: {self.enemigo.get_nombre()} | HP: {self.enemigo.get_vida()} | DEF: {self.enemigo.get_defensa()} |")
        self.__registrar("==========================================")
        
    def procesar_final_combate(self):
        niveles_agregados = randint(5, 15)
        self.aliado.subir_nivel(niveles_agregados)
        self.__registrar(f"\nTu pokemon ha recibido {niveles_agregados} niveles de XP.\n")
        self.aliado.solucionar_evolucion()

    def turno_aliado(self):
        try: 
            print(f"\n+--- Turno Aliado ({self.aliado.get_nombre()}) ---+")
            print("1. Pasar Turno.\t2. Ataque Normal.")
            print("3. Ataque Especial.\t4. Huir")
            opcion_aliado = int(input("Ingrese una opción: "))

            self.__registrar(f"\nEl aliado eligió la opción {opcion_aliado}.")
            if opcion_aliado == 1:
                self.__registrar("Turno pasado...")
            elif opcion_aliado == 2:
                self.__registrar(f"¡{self.aliado.get_nombre()} ha usado ataque normal!")
                dano = self.aliado.get_ataque()
                self.enemigo.procesar_dano(dano)
                self.__registrar(f"Has infligido {dano} pts. de daño a {self.enemigo.get_nombre()}.\n")
            elif opcion_aliado == 3:
                self.__registrar(f"¡{self.aliado.get_nombre()} ha usado {self.aliado.get_ataque_especial()}!")
                dano = int(self.aliado.get_ataque() * 1.8)
                self.enemigo.procesar_dano(dano)
                self.__registrar(f"Ha infligido {dano} pts. de daño a {self.enemigo.get_nombre()}.\n")
            else:
                self.__registrar("Has escapado el combate...\n\n")
                return False
            sleep(2)
            return True
        except ValueError:
            print("Error: Debe ingresar unicamente valores enteros!")



    def turno_enemigo(self):
        self.__registrar(f"+--- Turno Enemigo ({self.enemigo.get_nombre()}) ---+\n")
        opcion_enemigo = randint(1, 3)


        if opcion_enemigo == 1:
            self.__registrar(f"{self.enemigo.get_nombre()} ha utilizado ataque normal.")
            dano = self.enemigo.get_ataque()

        elif opcion_enemigo == 2:
            self.__registrar(f"{self.enemigo.get_nombre()} ha utilizado {self.enemigo.get_ataque_especial()}")
            dano = int(self.enemigo.get_ataque() * 1.6)
        else:
            self.__registrar(f"{self.enemigo.get_nombre()} no hizo nada y pasó turno.")
            return

        self.aliado.procesar_dano(dano)
        self.__registrar(f"El pokemon aliado ha recibido {dano} puntos de daño.\n")

    def imprimir_estado_combate(self):
        if self.aliado.sigue_vivo():
            self.__registrar("Has ganado el combate :D")
            self.__registrar(f"Has capturado al Pokemon \"{self.enemigo.get_nombre()}\".")
            return True
        self.__registrar("Perdiste")
        return False