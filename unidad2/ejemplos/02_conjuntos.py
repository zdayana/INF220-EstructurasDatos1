"""Unidad II: ADT Conjunto."""

from typing import Any


class ConjuntoADT:
    def __init__(self, elementos: list[Any] | None = None) -> None:
        self._datos = set(elementos or [])

    def agregar(self, elemento: Any) -> None:
        self._datos.add(elemento)

    def eliminar(self, elemento: Any) -> bool:
        if elemento in self._datos:
            self._datos.remove(elemento)
            return True
        return False

    def union(self, otro: "ConjuntoADT") -> "ConjuntoADT":
        return ConjuntoADT(list(self._datos | otro._datos))

    def interseccion(self, otro: "ConjuntoADT") -> "ConjuntoADT":
        return ConjuntoADT(list(self._datos & otro._datos))

    def diferencia(self, otro: "ConjuntoADT") -> "ConjuntoADT":
        return ConjuntoADT(list(self._datos - otro._datos))

    def diferencia_simetrica(self, otro: "ConjuntoADT") -> "ConjuntoADT":
        return ConjuntoADT(list(self._datos ^ otro._datos))

    def es_subconjunto(self, otro: "ConjuntoADT") -> bool:
        return self._datos.issubset(otro._datos)

    def __str__(self) -> str:
        return "{" + ", ".join(str(x) for x in sorted(self._datos, key=str)) + "}"


if __name__ == "__main__":
    a = ConjuntoADT([1, 2, 3, 4, 5])
    b = ConjuntoADT([3, 4, 5, 6, 7])

    print("A =", a)
    print("B =", b)
    print("A ∪ B =", a.union(b))
    print("A ∩ B =", a.interseccion(b))
    print("A - B =", a.diferencia(b))
    print("A △ B =", a.diferencia_simetrica(b))
