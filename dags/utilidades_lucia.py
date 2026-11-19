"""Funciones comunes de los ejercicios de Airflow con la biblioteca de Lucía."""
import csv
from pathlib import Path

CARPETA_DAGS = Path(__file__).parent
CARPETA_DATOS = CARPETA_DAGS / "datos"
CARPETA_SALIDA = CARPETA_DAGS / "salida"
ID_DUNE = "1"


def leer_csv(ruta):
    """Lee un CSV y devuelve una lista de diccionarios, una por fila."""
    with open(ruta, newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def escribir_csv(ruta, filas):
    """Guarda una lista de diccionarios como CSV, creando la carpeta si hace falta."""
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    columnas = list(filas[0].keys()) if filas else []
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(filas)


def contar_repetidos(filas, columna):
    """Cuenta cuántas filas sobran porque repiten el valor de una columna."""
    return len(filas) - len({fila[columna] for fila in filas})
