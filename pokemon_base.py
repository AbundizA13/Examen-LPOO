from abc import ABC, abstractmethod

class PokemonBase(ABC):
    _nombre : str
    _descripcion: str
    _ataque: int
    _defensa: int
    _vida: int
    _nivel: int
    _evolucion: int
    _atrapado: bool

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def get_ataque(self):
        return self._ataque

    def get_defensa(self):
        return self._defensa

    def get_vida(self):
        return self._vida

    def get_nivel(self):
        return self._nivel

    def get_evolucion(self):
        return self._evolucion

    def get_atrapado(self):
        return self._atrapado

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def actualizar(self, boost_ataque, boost_vida, boost_defensa):
        pass

    @abstractmethod
    def detalles_pokemon(self):
        pass

    def set_atrapado(self):
        self._atrapado = True

    @abstractmethod
    def entrenar(self):
        pass

    def __init__(self, nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado):
        self._nombre = nombre
        self._descripcion = descripcion
        self._ataque = ataque
        self._defensa = defensa
        self._vida = vida
        self._nivel = nivel
        self._evolucion = evolucion
        self._atrapado = atrapado


class Pokemon(PokemonBase):

    def actualizar(self, boost_ataque, boost_vida, boost_defensa):
        self.subir_ataque(boost_ataque)
        self.subir_vida(boost_vida)
        self.subir_defensa(boost_defensa)

    def detalles_pokemon(self):
        print(f"\"{self._nombre}\" {self._descripcion}.\n{self._vida} HP | Ataque: {self._ataque} | Defensa: {self._defensa} | Nivel: {self._nivel} | Evolucion: {self._evolucion} | Atrapado: {self._atrapado}.")

    def entrenar(self):
        self.subir_ataque(10)
        self.subir_vida(10)
        self.subir_defensa(10)
        self.subir_nivel(10)
        print(f"El pokemon {self._nombre} ha entrenado... Ataque +10, Vida +10, Defensa +10, Nivel +10")

        self.solucionar_evolucion()

    def solucionar_evolucion(self):
        if self._nivel >= 100 and self._evolucion < 3:
            self._nivel = 0
            self._evolucion += 1
            nombre_antiguo = self._nombre
            self._nombre = self.obtener_nombre_evolucion()
            print(f"\nEl pokemon {nombre_antiguo} ha evolucionado a {self._nombre}\n")
            input("ENTER para continuar.\n")

    def obtener_nombre_evolucion(self):
        pass

    def hablar(self):
        print(f"[Un pokemon está hablando] {self._nombre}... {self._nombre}!")

    def sigue_vivo(self):
        if self._vida <= 0:
            return False
        return True

    def eliminar_defensa(self):
        self._defensa = 0

    def subir_ataque(self, incremento):
        self._ataque += incremento
        if self._ataque > 1000:
            self._ataque = 1000

    def subir_defensa(self, incremento):
        self._defensa += incremento
        if self._defensa > 1000:
            self._defensa = 1000

    def subir_vida(self, incremento):
        self._vida += incremento
        if self._vida > 1000:
            self._vida = 1000

    def reducir_vida(self, decremento):
        self._vida -= decremento
        if self._vida < 0:
            self._vida = 0

    def subir_nivel(self, incremento):
        self._nivel += incremento
        if self._nivel > 1000:
            self._nivel = 1000

    def procesar_dano(self, dano):
        if dano > self._defensa:
            dano_sobrante = dano - self._defensa
            self.eliminar_defensa()
            self.reducir_vida(dano_sobrante)
        else:
            self._defensa -= dano

    #Constructor para Pókemon por defecto, su nivel y evolución empiezan en el mínimo | No atrapado por defecto
    def __init__(self, nombre, descripcion, ataque, defensa, vida , nivel = 1, evolucion = 1, atrapado = False):
        super().__init__(nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado)

class PokemonAgua(Pokemon):
    __evoluciones = ["Squirtle", "Wartortle", "Blastoise"]
    __ataque_especial = "Latigazo"

    def __init__(self, ataque, defensa, vida):
        super().__init__(self.__evoluciones[0], "Rocía espuma con gran fuerza por su boca.",ataque,defensa,vida)

    def obtener_nombre_evolucion(self):
        return self.__evoluciones[self._evolucion - 1]

    def get_ataque_especial(self):
        return self.__ataque_especial

class PokemonFuego(Pokemon):
    __evoluciones = ["Charmander", "Charmeleon", "Charizard"]
    __ataque_especial = "Lanzallamas"


    def __init__(self, ataque, defensa, vida):
        super().__init__(self.__evoluciones[0], "Prefiere claramente los lugares calientes.",ataque,defensa,vida)

    def obtener_nombre_evolucion(self):
        return self.__evoluciones[self._evolucion - 1]

    def get_ataque_especial(self):
        return self.__ataque_especial

class PokemonElectrico(Pokemon):
    __evoluciones = ["Pichu", "Pikachu", "Raichu"]
    __ataque_especial = "Impactrueno"

    def __init__(self, ataque, defensa, vida):
        super().__init__(self.__evoluciones[0], "Descarga energía de forma espontánea cuando se altera.",ataque,defensa,vida)

    def obtener_nombre_evolucion(self):
        return self.__evoluciones[self._evolucion-1]

    def get_ataque_especial(self):
        return self.__ataque_especial

class PokemonHierba(Pokemon):
    __evoluciones = ["Bulbasaur", "Ivysaur", "Venusaur"]
    __ataque_especial = "Hidrobomba"

    def __init__(self, ataque, defensa, vida):
        super().__init__(self.__evoluciones[0], "Una extraña semilla fue plantada en su espalda al nacer.",ataque,defensa,vida)

    def obtener_nombre_evolucion(self):
        return self.__evoluciones[self._evolucion - 1]

    def get_ataque_especial(self):
        return self.__ataque_especial