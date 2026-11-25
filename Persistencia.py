import os
import sqlite3

from pokemon_base import Pokemon, PokemonAgua, PokemonFuego, PokemonElectrico, PokemonHierba

class Partida:

    def __init__(self, id_partida: int, nombre: str, principal: Pokemon = None, creados: list = None, capturados: list = None):
        self.__id_partida = id_partida
        self.__nombre = nombre
        self.__principal = principal
        self.__creados = creados if creados is not None else []
        self.__capturados = capturados if capturados is not None else []


    def get_id(self):
        return self.__id_partida
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_pkm_principal(self):
        return self.__principal
    def set_pkm_principal(self, pkm_principal:Pokemon):
        self.__principal = pkm_principal
    def get_pkm_creados(self):
        return self.__creados
    def get_pkm_capturados(self):
        return self.__capturados

TIPO_CLASES = {
    "fuego": PokemonFuego,
    "agua": PokemonAgua,
    "electrico": PokemonElectrico,
    "hierba": PokemonHierba
}

class BaseDatos:
    __RUTA_BD = "./db/pokedex.db"
    #conexion = None

    def __conectar(self):
        os.makedirs(os.path.dirname(self.__RUTA_BD), exist_ok=True)
        conexion = sqlite3.connect(self.__RUTA_BD)
        conexion.execute("PRAGMA foreign_keys = ON;")
        return conexion



    def iniciar(self):
        conexion = self.__conectar()
        try:
            cursor = conexion.cursor()


            cursor.execute('''CREATE TABLE IF NOT EXISTS partidas(
                id_partida INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL
            )''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS pokemones (
                id_pokemon INTEGER PRIMARY KEY AUTOINCREMENT,
                id_partida INTEGER NOT NULL,
                rol TEXT NOT NULL CHECK (rol IN ('principal','creado','capturado')),
                tipo TEXT NOT NULL CHECK (tipo IN ('fuego','agua','electrico','hierba')),
                hp INTEGER,
                ataque INTEGER,
                defensa INTEGER,
                nivel INTEGER,
                evolucion INTEGER NOT NULL CHECK (evolucion BETWEEN 1 AND 3),
                atrapado INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (id_partida) REFERENCES partidas(id_partida)
            )''')

            conexion.commit()
        finally:
            conexion.close()


    #A partir de un objeto, lo escribe en la base de datos
    def __guardar_pokemon(self, pokemon: Pokemon, id_partida: int, rol: str, conexion):
        if rol not in ['principal', 'creado', 'capturado']:
            print("Se intentó guardar un pokemon con un rol desconocido.\nError en \"_guardar_pokemon()\".")
            return

        # Se asigna id al pokemon en la base de datos (NO necesita ID)

        cursor = conexion.cursor()
        cursor.execute(
            """
            INSERT INTO pokemones (id_partida, rol, tipo, hp, ataque, defensa, nivel, evolucion, atrapado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (id_partida,
                  rol.lower(),
                  pokemon.get_tipo().lower(),
                  pokemon.get_vida(),
                  pokemon.get_ataque(),
                  pokemon.get_defensa(),
                  pokemon.get_nivel(),
                  pokemon.get_evolucion(),
                  int(pokemon.get_atrapado())
                  )
        )

    #Borra el slot de una partida y lo rellena con el objeto Partida
    def guardar_partida(self, partida:Partida):
        id_partida = partida.get_id()
        conexion = self.__conectar()
        try:

            cursor = conexion.cursor()
            cursor.execute(
                """
                DELETE FROM pokemones WHERE id_partida = ?
                """,(id_partida,)
            )
            cursor.execute(
                """
                INSERT INTO partidas (id_partida, nombre) VALUES (?, ?)
                ON CONFLICT(id_partida) DO UPDATE SET nombre = excluded.nombre""",
                (id_partida,partida.get_nombre())
            )
            self.__guardar_pokemon(partida.get_pkm_principal(), id_partida, "principal",conexion)

            for pkm in partida.get_pkm_creados():
                self.__guardar_pokemon(pkm, id_partida, "creado",conexion)

            for pkm in partida.get_pkm_capturados():
                self.__guardar_pokemon(pkm, id_partida, "capturado",conexion)

            conexion.commit()
            return True
        except (sqlite3.Error, ValueError) as e:
            conexion.rollback()
            print(f"No se pudo guardar la partida: {e}")
            return False
        finally:
            conexion.close()

    def obtener_partida(self, id_partida:int):
        conexion = self.__conectar()
        try:
            #Permite hacer una diccionario en vez de una tupla normal
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            #PARTIDA
            cursor.execute("SELECT nombre FROM partidas WHERE id_partida = ?",(id_partida,))
            fila_partida = cursor.fetchone()
            if fila_partida is None:
                return None
            #partida encontrada - POKEMONS
            cursor.execute("SELECT * FROM pokemones WHERE id_partida = ?",(id_partida,))
            principal = None
            creados = []
            capturados = []
            #Saca todos los pokemons en la partida
            for fila in cursor.fetchall():
                rol = fila['rol']
                pkm = self.__fila_a_pokemon(fila)
                if rol == "principal":principal=pkm
                elif rol == "creado": creados.append(pkm)
                else: capturados.append(pkm)

            if principal is None:
                raise ValueError("La partida no tiene Pokemon principal.")
            return Partida(id_partida, fila_partida["nombre"], principal, creados, capturados)
        except (sqlite3.Error, ValueError) as e:
            print(f"No se pudo cargar la partida #{id_partida}: {e}")
            return None
        finally:
            conexion.close()

    def existe_partida(self, id_partida:int) -> bool:
        conexion = self.__conectar()
        try:
            cursor = conexion.execute("SELECT 1 FROM partidas WHERE id_partida = ?",(id_partida,))
            return cursor.fetchone() is not None
        finally:
            conexion.close()

    def __fila_a_pokemon(self, fila):
        clasePkm = TIPO_CLASES.get(fila["tipo"])
        if clasePkm is None:
            raise ValueError(f"Tipo desconocido en la base de datos: {fila['tipo']}")

        pokemon = clasePkm(fila["ataque"], fila["defensa"], fila["hp"])
        pokemon.restaurar_estado(fila["nivel"], fila["evolucion"], fila["atrapado"])
        return pokemon

    def obtener_output_menu_partidas(self) -> [str]:
        estado_partidas = []
        for n_partida in range(1,4):
            if self.existe_partida(n_partida):
                partida = self.obtener_partida(n_partida)
                estado_partidas.append(f"Espacio #{n_partida}: \"{partida.get_nombre()}\".")
            else:
                estado_partidas.append(f"Espacio #{n_partida}: VACIO")
        return estado_partidas
