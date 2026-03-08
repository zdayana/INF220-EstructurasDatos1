"""Unidad IV: medición simple de tiempos (complejidad empírica)."""

from timeit import timeit


def medir_insercion_inicio(n: int) -> tuple[float, float]:
    lista = list(range(n))
    t_list = timeit(lambda: lista.insert(0, -1), number=500)

    cola = list(range(n))
    t_append = timeit(lambda: cola.append(-1), number=500)
    return t_list, t_append


def medir_busqueda(n: int) -> tuple[float, float]:
    datos = list(range(n))
    objetivo = n - 1
    t_lineal = timeit(lambda: objetivo in datos, number=2000)

    tabla = {i: i for i in range(n)}
    t_hash = timeit(lambda: objetivo in tabla, number=2000)
    return t_lineal, t_hash


if __name__ == "__main__":
    print("n\tinsert(0)\tappend\t\tbusq_lista\tbusq_hash")
    for n in (1_000, 5_000, 10_000):
        t1, t2 = medir_insercion_inicio(n)
        t3, t4 = medir_busqueda(n)
        print(f"{n}\t{t1:.6f}\t{t2:.6f}\t{t3:.6f}\t{t4:.6f}")
