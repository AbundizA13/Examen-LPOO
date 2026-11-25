import os
import sqlite3

from pokemon_base import Pokemon

class Partida:
    #Almacena el estado completo de la partida para ser leido.
    def __init__(self,id_partida:int, nombre:str,principal:Pokemon,creados:list,capturados:list):
        self.__id_partida = id_partida
        self.__nombre = nombre
        self.__principal = principal
        self.__creados = creados
        self.__capturados = capturados

    def get_id(self):
        return self.__id_partida
    def get_nombre(self):
        return self.__nombre
    def get_pkm_principal(self):
        return self.__principal
    def get_pkm_creados(self):
        return self.__creados
    def get_pkm_capturados(self):
        return self.__capturados


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
                nivel INTEGER,
                evolucion INTEGER NOT NULL CHECK (evolucion BETWEEN 1 AND 3),
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
            INSERT INTO pokemones (id_partida, rol, tipo, hp, ataque, nivel, evolucion)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (id_partida,
                  rol.lower(),
                  pokemon.get_tipo().lower(),
                  pokemon.get_vida(),
                  pokemon.get_ataque(),
                  pokemon.get_nivel(),
                  pokemon.get_evolucion())
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

    def obtener_partida(self, ):
        pass


