"""Ejercicio 3: que el flujo avise cuando algo está raro (con un hueco para completar)."""
from datetime import datetime

from airflow.sdk import dag, task
from utilidades_lucia import CARPETA_DATOS, CARPETA_SALIDA, contar_repetidos, escribir_csv, leer_csv


@dag(
    dag_id="ej3_validacion",
    schedule=None,
    start_date=datetime(2026, 4, 1),
    catchup=False,
    tags=["ejercicio"],
)
def validacion():
    """Trae el archivo de abril, lo revisa y solo después lo limpia."""

    @task
    def traer():
        """Copia el archivo original de abril sin cambiarlo."""
        filas = leer_csv(CARPETA_DATOS / "prestamos_abril.csv")
        escribir_csv(CARPETA_SALIDA / "abril_bruto.csv", filas)
        print(f"Traje {len(filas)} filas")
        return len(filas)

    @task
    def validar_sin_repetidos(filas_traidas):
        """Debe fallar si el archivo trae filas con el mismo prestamo_id."""
        filas = leer_csv(CARPETA_SALIDA / "abril_bruto.csv")
        repetidas = contar_repetidos(filas, "prestamo_id")
        # TODO: si hay filas repetidas, detén el flujo con raise ValueError("...")
        print(f"Revisé {filas_traidas} filas y encontré {repetidas} repetidas")

    @task
    def limpiar():
        """Quita las filas repetidas y guarda el archivo limpio."""
        filas = leer_csv(CARPETA_SALIDA / "abril_bruto.csv")
        vistos = set()
        limpias = []
        for fila in filas:
            if fila["prestamo_id"] not in vistos:
                vistos.add(fila["prestamo_id"])
                limpias.append(fila)
        escribir_csv(CARPETA_SALIDA / "abril_limpio.csv", limpias)
        print(f"Quedaron {len(limpias)} filas limpias")

    validar_sin_repetidos(traer()) >> limpiar()


validacion()
