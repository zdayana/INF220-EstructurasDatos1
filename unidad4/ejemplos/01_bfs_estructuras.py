"""Unidad IV: BFS sobre árbol y grafo."""

from collections import deque


class NodoArbol:
    def __init__(self, valor: str) -> None:
        self.valor = valor
        self.hijos: list[NodoArbol] = []

    def agregar_hijo(self, hijo: "NodoArbol") -> None:
        self.hijos.append(hijo)


def bfs_arbol(raiz: NodoArbol | None) -> list[str]:
    if raiz is None:
        return []
    recorrido: list[str] = []
    cola = deque([raiz])
    while cola:
        actual = cola.popleft()
        recorrido.append(actual.valor)
        for hijo in actual.hijos:
            cola.append(hijo)
    return recorrido


def bfs_grafo(grafo: dict[str, list[str]], inicio: str) -> list[str]:
    visitados = {inicio}
    recorrido: list[str] = []
    cola = deque([inicio])
    while cola:
        nodo = cola.popleft()
        recorrido.append(nodo)
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    return recorrido


if __name__ == "__main__":
    a = NodoArbol("A")
    b, c, d = NodoArbol("B"), NodoArbol("C"), NodoArbol("D")
    a.agregar_hijo(b)
    a.agregar_hijo(c)
    b.agregar_hijo(d)
    print("BFS árbol:", bfs_arbol(a))

    grafo_demo = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": [],
    }
    print("BFS grafo:", bfs_grafo(grafo_demo, "A"))
