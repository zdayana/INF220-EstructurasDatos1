"""Unidad III: Bicola (Deque) dinámica."""

from collections import deque
from typing import Any


class Bicola:
    def __init__(self) -> None:
        self._datos: deque[Any] = deque()

    def insertar_frente(self, dato: Any) -> None:
        self._datos.appendleft(dato)

    def insertar_fondo(self, dato: Any) -> None:
        self._datos.append(dato)

    def eliminar_frente(self) -> Any:
        if self.esta_vacia():
            raise IndexError("Bicola vacía")
        return self._datos.popleft()

    def eliminar_fondo(self) -> Any:
        if self.esta_vacia():
            raise IndexError("Bicola vacía")
        return self._datos.pop()

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def __len__(self) -> int:
        return len(self._datos)

    def __str__(self) -> str:
        return "Bicola([" + ", ".join(str(x) for x in self._datos) + "])"


if __name__ == "__main__":
    d = Bicola()
    d.insertar_fondo(20)
    d.insertar_fondo(30)
    d.insertar_frente(10)
    print(d)
    print("eliminar_frente:", d.eliminar_frente())
    print("eliminar_fondo:", d.eliminar_fondo())
    print(d)
