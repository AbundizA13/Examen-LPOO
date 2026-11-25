"""
Bitácora de combates: un archivo .txt por día en ./logs/AAAA-MM-DD.txt

Uso esperado (en combate.py):
    from bitacora import Bitacora

    class Combate:
        def __init__(self, aliado, enemigo):
            ...
            self.bitacora = Bitacora()

        # Reemplazar cada print(...) del combate por:
        #     self.bitacora.registrar("texto")

Uso esperado (en Pookedex.py, opcion_3, después de ciclo_combate()):
    combate.bitacora.guardar(partida, resultado)

Este archivo YA FUNCIONA tal cual. Lo marcado con TODO es opcional/mejoras.
"""
import os
from datetime import datetime


class Bitacora:
    __CARPETA = "./logs"
    SEPARADOR = "=" * 50

    def __init__(self):
        self.__lineas = []
        self.__inicio = datetime.now()

    # ---------- Registro en memoria ----------
    def registrar(self, texto: str = "", mostrar: bool = True):
        """Imprime en pantalla (si mostrar=True) y guarda la línea en memoria."""
        if mostrar:
            print(texto)
        self.__lineas.append(str(texto))

    def titulo(self, texto: str):
        """Encabezado visual, ej. 'TURNO 3'."""
        self.registrar(f"\n{texto.center(len(self.SEPARADOR), '=')}")

    def separador(self):
        self.registrar("-" * len(self.SEPARADOR))

    def get_lineas(self):
        return list(self.__lineas)

    def limpiar(self):
        self.__lineas.clear()

    # ---------- Escritura a disco ----------
    def __ruta_del_dia(self) -> str:
        return os.path.join(self.__CARPETA, f"{datetime.now():%Y-%m-%d}.txt")

    def guardar(self, partida=None, resultado: str = "SIN RESULTADO") -> bool:
        """
        Agrega el combate actual al archivo del día (modo 'a': crea o añade).
        partida: objeto Partida (opcional). resultado: 'VICTORIA', 'DERROTA', 'HUIDA'...
        Regresa True si se guardó.
        """
        if not self.__lineas:
            return False

        if partida is not None:
            info_partida = f'Partida #{partida.get_id()} "{partida.get_nombre()}"'
        else:
            info_partida = "Partida desconocida"

        encabezado = (
            f"\n{'#' * 50}\n"
            f"{self.__inicio:%H:%M:%S} | {info_partida} | Resultado: {resultado}\n"
            f"{'#' * 50}\n"
        )
        try:
            os.makedirs(self.__CARPETA, exist_ok=True)
            with open(self.__ruta_del_dia(), "a", encoding="utf-8") as archivo:
                archivo.write(encabezado)
                archivo.write("\n".join(self.__lineas) + "\n")
            return True
        except OSError as e:
            print(f"No se pudo guardar la bitácora: {e}")
            return False

    # TODO (opcional): leer_dia(fecha) -> str  para mostrar el log desde el menú.


# Prueba rápida: python bitacora.py  -> crea ./logs/<hoy>.txt
if __name__ == "__main__":
    b = Bitacora()
    b.titulo(" TURNO 1 ")
    b.registrar("  Aliado : Charmander | HP 100 | DEF 10")
    b.registrar("  Enemigo: Squirtle   | HP  80 | DEF 5")
    b.separador()
    b.registrar("> Charmander usó Ataque normal (20 de ataque)")
    print("Guardado:", b.guardar(resultado="PRUEBA"))
