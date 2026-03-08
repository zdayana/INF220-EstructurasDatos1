"""Unidad III: Cola circular estática."""

from typing import Any


class ColaCircular:
    def __init__(self, capacidad: int) -> None:
        if capacidad <= 0:
            raise ValueError("Capacidad inválida")
        self._datos: list[Any | None] = [None] * capacidad
        self._capacidad = capacidad
        self._frente = 0
        self._fondo = 0
        self._tamanio = 0

    def encolar(self, dato: Any) -> None:
        if self._tamanio == self._capacidad:
            raise OverflowError("Cola llena")
        self._datos[self._fondo] = dato
        self._fondo = (self._fondo + 1) % self._capacidad
        self._tamanio += 1

    def desencolar(self) -> Any:
        if self._tamanio == 0:
            raise IndexError("Cola vacía")
        dato = self._datos[self._frente]
        self._datos[self._frente] = None
        self._frente = (self._frente + 1) % self._capacidad
        self._tamanio -= 1
        return dato

    def frente(self) -> Any:
        if self._tamanio == 0:
            raise IndexError("Cola vacía")
        return self._datos[self._frente]

    def esta_vacia(self) -> bool:
        return self._tamanio == 0

    def __str__(self) -> str:
        if self.esta_vacia():
            return "Cola([])"
        elementos = []
        indice = self._frente
        for _ in range(self._tamanio):
            elementos.append(str(self._datos[indice]))
            indice = (indice + 1) % self._capacidad
        return "Cola([" + ", ".join(elementos) + "])"


if __name__ == "__main__":
    cola = ColaCircular(5)
    cola.encolar(10)
    cola.encolar(20)
    cola.encolar(30)
    print(cola)
    print("Sale:", cola.desencolar())
    cola.encolar(40)
    cola.encolar(50)
    cola.encolar(60)
    print(cola)
