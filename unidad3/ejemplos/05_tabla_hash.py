"""Unidad III: Tabla hash con encadenamiento."""

from typing import Any


class TablaHash:
    def __init__(self, capacidad: int = 8) -> None:
        self._tabla: list[list[tuple[Any, Any]]] = [[] for _ in range(capacidad)]
        self._tamanio = 0

    def _indice(self, clave: Any) -> int:
        return hash(clave) % len(self._tabla)

    def insertar(self, clave: Any, valor: Any) -> None:
        bucket = self._tabla[self._indice(clave)]
        for i, (k, _) in enumerate(bucket):
            if k == clave:
                bucket[i] = (clave, valor)
                return
        bucket.append((clave, valor))
        self._tamanio += 1

    def buscar(self, clave: Any) -> Any | None:
        bucket = self._tabla[self._indice(clave)]
        for k, v in bucket:
            if k == clave:
                return v
        return None

    def eliminar(self, clave: Any) -> bool:
        bucket = self._tabla[self._indice(clave)]
        for i, (k, _) in enumerate(bucket):
            if k == clave:
                bucket.pop(i)
                self._tamanio -= 1
                return True
        return False

    def __len__(self) -> int:
        return self._tamanio

    def __str__(self) -> str:
        pares = []
        for bucket in self._tabla:
            pares.extend(bucket)
        contenido = ", ".join(f"{k!r}: {v!r}" for k, v in pares)
        return "{" + contenido + "}"


if __name__ == "__main__":
    tabla = TablaHash()
    tabla.insertar("BO", "Bolivia")
    tabla.insertar("AR", "Argentina")
    tabla.insertar("PY", "Paraguay")

    print(tabla)
    print("buscar('AR'):", tabla.buscar("AR"))
    print("eliminar('BO'):", tabla.eliminar("BO"))
    print(tabla)
