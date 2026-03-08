"""Unidad IV: DFS recursivo e iterativo."""


def dfs_recursivo(grafo: dict[str, list[str]], inicio: str) -> list[str]:
    visitados: set[str] = set()
    recorrido: list[str] = []

    def visitar(nodo: str) -> None:
        visitados.add(nodo)
        recorrido.append(nodo)
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitar(vecino)

    visitar(inicio)
    return recorrido


def dfs_iterativo(grafo: dict[str, list[str]], inicio: str) -> list[str]:
    visitados: set[str] = set()
    recorrido: list[str] = []
    pila = [inicio]

    while pila:
        nodo = pila.pop()
        if nodo in visitados:
            continue
        visitados.add(nodo)
        recorrido.append(nodo)
        for vecino in reversed(grafo.get(nodo, [])):
            if vecino not in visitados:
                pila.append(vecino)
    return recorrido


if __name__ == "__main__":
    grafo_demo = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": [],
    }
    print("DFS recursivo:", dfs_recursivo(grafo_demo, "A"))
    print("DFS iterativo:", dfs_iterativo(grafo_demo, "A"))
