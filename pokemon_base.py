from abc import ABC, abstractmethod

class Pokemon(ABC):
    nombre = "Sin Pokemon"
    descripcion = "No descripcion"
    ataque : int
    defensa : int
    vida : int
    nivel : int
    evolucion : int
    atrapado : bool

    @abstractmethod
    def hablar(self):
        pass

    def actualizar(self):
        self.subir_ataque()
        self.subir_vida()
        self.subir_defensa()

    @abstractmethod
    def detalles_pokemon(self):
        pass

    @abstractmethod
    def entrenar(self):
        pass

    def subir_ataque(self):
        self.ataque += 20

    def subir_defensa(self):
        self.defensa += 20

    def subir_vida(self):
        self.vida += 20

    def __init__(self, nombre, descripcion, ataque, defensa, vida):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.nivel = 1
        self.evolucion = 0
        self.atrapado = False

class PokemonEspecializado(Pokemon):
    ataque_especial = ""

    def __init__(self, nombre, descripcion, ataque, defensa, vida, ataque_especial):
        super().__init__(nombre, descripcion, ataque, defensa, vida)
        self.ataque_especial = ataque_especial
    
    def hablar(self):
        print(f"{self.nombre} ha hablado.")

    def detalles_pokemon(self):
        pass

    def entrenar(self):
        pass