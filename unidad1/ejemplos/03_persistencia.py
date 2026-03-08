"""Unidad I: Persistencia con JSON y Pickle."""

import json
import pickle
from pathlib import Path
from typing import Any


def guardar_json(datos: list[dict[str, Any]], ruta: Path) -> None:
    with ruta.open("w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)


def cargar_json(ruta: Path) -> list[dict[str, Any]]:
    with ruta.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_pickle(objeto: Any, ruta: Path) -> None:
    with ruta.open("wb") as archivo:
        pickle.dump(objeto, archivo)


def cargar_pickle(ruta: Path) -> Any:
    with ruta.open("rb") as archivo:
        return pickle.load(archivo)


if __name__ == "__main__":
    base = Path(__file__).parent
    ruta_json = base / "alumnos_demo.json"
    ruta_pkl = base / "alumnos_demo.pkl"

    alumnos = [
        {"nombre": "Ana", "nota": 87},
        {"nombre": "Luis", "nota": 92},
        {"nombre": "Sofía", "nota": 78},
    ]

    guardar_json(alumnos, ruta_json)
    guardar_pickle(alumnos, ruta_pkl)

    print("JSON:", cargar_json(ruta_json))
    print("Pickle:", cargar_pickle(ruta_pkl))
