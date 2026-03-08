"""Unidad 0: Interfaces con ABC."""

from abc import ABC, abstractmethod
from collections import deque
from typing import Any


class EstructuraLineal(ABC):
    """Interfaz base para estructuras lineales."""

    @abstractmethod
    def insertar(self, dato: Any) -> None:
        pass

    @abstractmethod
    def eliminar(self) -> Any:
        pass

    @abstractmethod
    def esta_vacia(self) -> bool:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass


class Pila(EstructuraLineal):
    def __init__(self) -> None:
        self._datos: list[Any] = []

    def insertar(self, dato: Any) -> None:
        self._datos.append(dato)

    def eliminar(self) -> Any:
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self._datos.pop()

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def __len__(self) -> int:
        return len(self._datos)


class Cola(EstructuraLineal):
    def __init__(self) -> None:
        self._datos: deque[Any] = deque()

    def insertar(self, dato: Any) -> None:
        self._datos.append(dato)

    def eliminar(self) -> Any:
        if self.esta_vacia():
            raise IndexError("Cola vacía")
        return self._datos.popleft()

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def __len__(self) -> int:
        return len(self._datos)


def consumir(estructura: EstructuraLineal) -> list[Any]:
    """Usa la interfaz sin conocer implementación concreta."""
    salida = []
    while not estructura.esta_vacia():
        salida.append(estructura.eliminar())
    return salida


if __name__ == "__main__":
    pila = Pila()
    cola = Cola()
    for valor in [10, 20, 30]:
        pila.insertar(valor)
        cola.insertar(valor)

    print("Pila (LIFO):", consumir(pila))
    print("Cola (FIFO):", consumir(cola))
