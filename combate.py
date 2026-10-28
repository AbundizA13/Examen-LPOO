"""
Vamos a separar los menús del main a un menú compacto de combate

Los demás menús seguirán viviendo en Pookedex.py
"""
from pokemon_base import Pokemon
from random import randint


class Combate:
    aliado = None
    enemigo = None

    def __init__(self, aliado: Pokemon, enemigo: Pokemon):
        self.aliado = aliado
        self.enemigo = enemigo

    #Se llamará SOLO una vez, cada que inicie un nuevo combate
    #Este se encargará de acabar cuando uno de los dos pokemons muera.
    def ciclo_combate(self):
        print("\n-+--|-----Combate-----|--+-")
        #Mientras ambos pokemons sigan vivos...
        while self.enemigo.sigue_vivo() and self.aliado.sigue_vivo():
            print(f"Aliado: {self.aliado.get_nombre()} - HP: {self.aliado.get_vida()}")
            print(f"Enemigo: {self.enemigo.get_nombre()} - HP: {self.enemigo.get_vida()}")
            if not self.turno_aliado():
                print("Has escapado del combate...\n")
                return
            if self.enemigo.sigue_vivo():
                self.turno_enemigo()
        if self.imprimir_estado_combate():
            self.procesar_final_combate()
            self.aliado.solucionar_evolucion()
            return True

        return False

    def procesar_final_combate(self):
        niveles_agregados = randint(5, 15)
        self.aliado.subir_nivel(niveles_agregados)
        print(f"\nTu pokemon ha recibido {niveles_agregados} niveles de XP.\n")
        self.aliado.solucionar_evolucion()

    def turno_aliado(self):
        print(f"+--- Turno Aliado ({self.aliado.get_nombre()}) ---+\n")
        print("1. Pasar Turno.\t2. Ataque Normal.")
        print("3. Ataque Especial.\t4. Huir")
        opcion_aliado = int(input("Ingrese una opción: "))

        if opcion_aliado == 1:
            print("Turno pasado...")
        elif opcion_aliado == 2:
            print(f"¡{self.aliado.get_nombre()} ha usado ataque normal!")
            dano = self.aliado.get_ataque()
            self.enemigo.procesar_dano(dano)
            print(f"Has infligido {dano} pts. de daño a {self.enemigo.get_nombre()}.\n")
        elif opcion_aliado == 3:
            print(f"¡{self.aliado.get_nombre()} ha usado {self.aliado.get_ataque_especial()}!")
            dano = int(self.aliado.get_ataque() * 1.8)
            self.enemigo.procesar_dano(dano)
            print(f"Ha infligido {dano} pts. de daño a {self.enemigo.get_nombre()}.\n")
        else:
            print("Has escapado el combate...\n\n")
            return False
        return True





    def turno_enemigo(self):
        print(f"+--- Turno Enemigo ({self.enemigo.get_nombre()}) ---+\n")
        opcion_enemigo = randint(1, 3)


        if opcion_enemigo == 1:
            print(f"{self.enemigo.get_nombre()} ha utilizado ataque normal.")
            dano = self.enemigo.get_ataque()
        elif opcion_enemigo == 2:
            print(f"{self.enemigo.get_nombre()} ha utilizado {self.enemigo.get_ataque_especial()}")
            dano = int(self.enemigo.get_ataque() * 1.6)
        else:
            print(f"{self.enemigo.get_nombre()} no hizo nada y pasó turno.")
            return

        self.aliado.procesar_dano(dano)

    #Devuelve True si el jugador ganó
    def imprimir_estado_combate(self):
        if self.aliado.sigue_vivo():
            print("Has ganado el combate :D")
            print(f"Has capturado al Pokemon \"{self.enemigo.get_nombre()}\".")
            return True
        return False