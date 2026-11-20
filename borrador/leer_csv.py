import csv
import os

COLUMNAS = {"timestamp", "interfaz", "bytes_tx", "bytes_rx", "paquetes_descartados"}

def leer_csv(ruta):
    if not ruta.lower().endswith(".csv"):
        raise ValueError("El archivo debe tener extensión .csv")
    if not os.path.isfile(ruta):
        raise FileNotFoundError("No se encontró el archivo seleccionado")

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        faltantes = COLUMNAS - set(lector.fieldnames or [])
        if faltantes:
            raise ValueError("Faltan columnas: " + ", ".join(sorted(faltantes)))

        datos = {}
        for fila in lector:
            datos.setdefault(fila["interfaz"], []).append({
                "timestamp": fila["timestamp"],
                "bytes_tx": int(fila["bytes_tx"]),
                "bytes_rx": int(fila["bytes_rx"]),
                "paquetes_descartados": int(fila["paquetes_descartados"]),
            })

    if not datos:
        raise ValueError("El archivo no contiene registros")
    return datos