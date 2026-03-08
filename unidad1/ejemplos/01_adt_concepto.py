"""Unidad I: ADT, abstracción vs implementación."""

from abc import ABC, abstractmethod
from typing import Any


class ADTPila(ABC):
    @abstractmethod
    def apilar(self, dato: Any) -> None:
        pass

    @abstractmethod
    def desapilar(self) -> Any:
        pass

    @abstractmethod
    def tope(self) -> Any:
        pass

    @abstractmethod
    def esta_vacia(self) -> bool:
        pass


class PilaArray(ADTPila):
    def __init__(self) -> None:
        self._datos: list[Any] = []

    def apilar(self, dato: Any) -> None:
        self._datos.append(dato)

    def desapilar(self) -> Any:
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self._datos.pop()

    def tope(self) -> Any:
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self._datos[-1]

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0


class _Nodo:
    def __init__(self, dato: Any, sig: "_Nodo | None" = None) -> None:
        self.dato = dato
        self.sig = sig


class PilaLista(ADTPila):
    def __init__(self) -> None:
        self._tope: _Nodo | None = None

    def apilar(self, dato: Any) -> None:
        self._tope = _Nodo(dato, self._tope)

    def desapilar(self) -> Any:
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        dato = self._tope.dato
        self._tope = self._tope.sig
        return dato

    def tope(self) -> Any:
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self._tope.dato

    def esta_vacia(self) -> bool:
        return self._tope is None


def usar_pila(pila: ADTPila) -> list[Any]:
    for x in [1, 2, 3]:
        pila.apilar(x)
    return [pila.desapilar(), pila.desapilar(), pila.desapilar()]


if __name__ == "__main__":
    print("Array:", usar_pila(PilaArray()))
    print("Lista:", usar_pila(PilaLista()))
