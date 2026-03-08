"""Unidad II: ADT Polinomio."""

from collections import defaultdict


class Polinomio:
    def __init__(self) -> None:
        self._terminos: dict[int, float] = {}

    def agregar_termino(self, coeficiente: float, exponente: int) -> None:
        if exponente < 0:
            raise ValueError("Exponente inválido")
        nuevo = self._terminos.get(exponente, 0.0) + coeficiente
        if nuevo == 0:
            self._terminos.pop(exponente, None)
        else:
            self._terminos[exponente] = nuevo

    def evaluar(self, x: float) -> float:
        return sum(coef * (x**exp) for exp, coef in self._terminos.items())

    def sumar(self, otro: "Polinomio") -> "Polinomio":
        resultado = Polinomio()
        acumulado = defaultdict(float)
        for exp, coef in self._terminos.items():
            acumulado[exp] += coef
        for exp, coef in otro._terminos.items():
            acumulado[exp] += coef
        for exp, coef in acumulado.items():
            resultado.agregar_termino(coef, exp)
        return resultado

    def derivar(self) -> "Polinomio":
        derivada = Polinomio()
        for exp, coef in self._terminos.items():
            if exp > 0:
                derivada.agregar_termino(coef * exp, exp - 1)
        return derivada

    def __str__(self) -> str:
        if not self._terminos:
            return "0"
        piezas = []
        for exp in sorted(self._terminos, reverse=True):
            coef = self._terminos[exp]
            if exp == 0:
                piezas.append(f"{coef:+g}")
            elif exp == 1:
                piezas.append(f"{coef:+g}x")
            else:
                piezas.append(f"{coef:+g}x^{exp}")
        return " ".join(piezas).lstrip("+")


if __name__ == "__main__":
    p = Polinomio()
    p.agregar_termino(3, 2)
    p.agregar_termino(5, 1)
    p.agregar_termino(-1, 0)

    q = Polinomio()
    q.agregar_termino(1, 2)
    q.agregar_termino(2, 0)

    print("P(x) =", p)
    print("Q(x) =", q)
    print("P+Q =", p.sumar(q))
    print("P'(x)=", p.derivar())
    print("P(2) =", p.evaluar(2))
