"""Unidad II: Matriz dispersa con diccionario de coordenadas."""


class MatrizDispersa:
    def __init__(self, filas: int, columnas: int) -> None:
        if filas <= 0 or columnas <= 0:
            raise ValueError("Dimensiones inválidas")
        self._filas = filas
        self._columnas = columnas
        self._datos: dict[tuple[int, int], float] = {}

    def _validar(self, fila: int, columna: int) -> None:
        if not (0 <= fila < self._filas and 0 <= columna < self._columnas):
            raise IndexError("Posición fuera de rango")

    def establecer(self, fila: int, columna: int, valor: float) -> None:
        self._validar(fila, columna)
        if valor == 0:
            self._datos.pop((fila, columna), None)
        else:
            self._datos[(fila, columna)] = valor

    def obtener(self, fila: int, columna: int) -> float:
        self._validar(fila, columna)
        return self._datos.get((fila, columna), 0.0)

    def transponer(self) -> "MatrizDispersa":
        resultado = MatrizDispersa(self._columnas, self._filas)
        for (fila, columna), valor in self._datos.items():
            resultado.establecer(columna, fila, valor)
        return resultado

    def densidad(self) -> float:
        total = self._filas * self._columnas
        return (len(self._datos) / total) * 100

    def __str__(self) -> str:
        return (
            f"MatrizDispersa({self._filas}x{self._columnas}, "
            f"no_ceros={len(self._datos)}, densidad={self.densidad():.2f}%)"
        )


if __name__ == "__main__":
    matriz = MatrizDispersa(5, 5)
    matriz.establecer(0, 2, 5)
    matriz.establecer(2, 1, 8)
    matriz.establecer(4, 3, 3)

    print(matriz)
    print("(2,1)=", matriz.obtener(2, 1))
    print("(1,1)=", matriz.obtener(1, 1))
    print("Transpuesta:", matriz.transponer())
