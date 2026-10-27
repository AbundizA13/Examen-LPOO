"""
Vamos a separar los menús del main a un menú compacto de combate

Los demás menús seguirán viviendo en Pookedex.py
"""
from Pokedex.pokemon_base import Pokemon


class Combate:
    aliado = None
    enemigo = None

    def __init__(self, aliado: Pokemon, enemigo: Pokemon):
        self.aliado = aliado
        self.enemigo = enemigo

    #Se llamará SOLO una vez, cada que inicie un nuevo combate
    #Este se encargará de acabar cuando uno de los dos pokemons muera.
    def ciclo_combate(self):
        print("\n-+--|-----Combate-----|--+-\n")
        #Mientras ambos pokemons sigan vivos...
        while self.enemigo.sigue_vivo() and self.aliado.sigue_vivo():
            if not self.turno_aliado(): break
            self.turno_enemigo()


    def turno_aliado(self):
        print(f"+--- Turno Aliado ({self.aliado.nombre}) ---+\n")
        print("1. Pasar Turno.\t2. Ataque Normal.")
        print("3. Ataque Especial.\t4. Huir")
        opcion_aliado = int(input("Ingrese una opción: "))

        if opcion_aliado == 1:
            print("Turno pasado...")
        elif opcion_aliado == 2:
            print(f"¡{self.aliado.nombre} ha usado ataque normal!")
            dano = self.aliado.ataque
            self.procesar_dano(dano, self.enemigo)
            print(f"Has infligido {dano} pts. de daño a {self.enemigo.nombre}.\n")
        elif opcion_aliado == 3:
            print(f"¡{self.aliado.nombre} ha usado {self.aliado.ataque_especial}!")
            dano = int(self.aliado.ataque * 1.8)
            self.procesar_dano(dano, self.enemigo)
            print(f"Ha infligido {dano} pts. de daño a {self.enemigo.nombre}.\n")
        else:
            print("Has escapado el combate...\n\n")
            return False
        return True





    def turno_enemigo(self):
        print(f"+--- Turno Enemigo ({self.enemigo.nombre}) ---+\n")
        opcion_enemigo = randint(1, 3)


        if opcion_enemigo == 1:
            print(f"{self.enemigo.nombre} ha utilizado ataque normal.")
            dano = self.enemigo.ataque
        elif opcion_enemigo == 2:
            print(f"{self.enemigo.nombre} ha utilizado {self.enemigo.ataque_especial}")
            dano = int(self.enemigo.ataque * 1.6)
        else:
            print(f"{self.enemigo.nombre} no hizo nada y pasó turno.")
            return

        self.procesar_dano(dano, self.aliado)

    def procesar_dano(self, dano: int, receptor: Pokemon):
        if dano > receptor.defensa:
            dano_sobrante = dano - receptor.defensa
            receptor.eliminar_defensa()
            receptor.vida -= dano_sobrante
        else:
            receptor.defensa -= dano
