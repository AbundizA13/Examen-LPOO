from abc import ABC, abstractmethod

class PokemonBase(ABC):
    nombre : str
    descripcion: str
    ataque: int
    defensa: int
    vida: int
    nivel: int
    evolucion: int
    atrapado: bool

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def actualizar(self, boost_ataque, boost_vida, boost_defensa):
        pass

    @abstractmethod
    def detalles_pokemon(self):
        pass


    @abstractmethod
    def entrenar(self):
        pass

    def __init__(self, nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.nivel = nivel
        self.evolucion = evolucion
        self.atrapado = atrapado


class Pokemon(PokemonBase):

    def actualizar(self, boost_ataque, boost_vida, boost_defensa):
        self.subir_ataque(boost_ataque)
        self.subir_vida(boost_vida)
        self.subir_defensa(boost_defensa)

    def detalles_pokemon(self):
        print(f"\"{self.nombre}\" {self.descripcion}.\n{self.vida} HP | Ataque: {self.ataque} | Defensa: {self.defensa} | Nivel: {self.nivel} | Evolucion: {self.evolucion} | Atrapado: {self.atrapado}.")


    def entrenar(self):
        self.subir_ataque(10)
        self.subir_vida(10)
        self.subir_defensa(10)
        self.subir_nivel(10)
        print(f"El pokemon {self.nombre} ha entrenado... Ataque +10, Vida +10, Defensa +10, Nivel +10")

        if self.nivel >= 100 and self.evolucion < 4: #Ha llegado al nivel para evolucionar
            self.nivel = 0
            self.evolucion += 1
            nombre_antiguo = self.nombre
            self.nombre = self.obtener_nombre_evolucion()
            print(f"El pokemon {nombre_antiguo} a evolucionado a {self.nombre}.")

    def obtener_nombre_evolucion(self):
        return self.nombre

    def hablar(self):
        print(f"[Un pokemon está hablando] {self.nombre}... {self.nombre}!")


    def subir_ataque(self, incremento):
        self.ataque += incremento

    def subir_defensa(self, incremento):
        self.defensa += incremento

    def subir_vida(self, incremento):
        self.vida += incremento

    def subir_nivel(self, incremento):
        self.nivel += incremento

    #Constructor para Pókemon por defecto, su nivel y evolución empiezan en el mínimo | No atrapado por defecto
    def __init__(self, nombre, descripcion, ataque, defensa, vida , nivel = 1, evolucion = 1, atrapado = False):
        super().__init__(nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado)

class PokemonAgua(Pokemon):
    evoluciones = ["Squirtle", "Wartortle", "Blastoise"]

    def __init__(self, ataque, defensa, vida):
        super().__init__(self.evoluciones[0], "Rocía espuma con gran fuerza por su boca.",ataque,defensa,vida)

class PokemonFuego(Pokemon):
    evoluciones = ["Charmander", "Charmeleon", "Charizard"]


    def __init__(self, ataque, defensa, vida):
        super().__init__(self.evoluciones[0], "Prefiere claramente los lugares calientes.",ataque,defensa,vida)

class PokemonElectrico(Pokemon):
    evoluciones = ["Pichu", "Pikachu", "Raichu"]

    def __init__(self, ataque, defensa, vida):
        super().__init__(self.evoluciones[0], "Descarga energía de forma espontánea cuando se altera.",ataque,defensa,vida)

class PokemonHierba(Pokemon):
    evoluciones = ["Bulbasaur", "Ivysaur", "Venusaur"]

    def __init__(self, ataque, defensa, vida):
        super().__init__(self.evoluciones[0], "Una extraña semilla fue plantada en su espalda al nacer.",ataque,defensa,vida)