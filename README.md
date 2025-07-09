# Algoritmo de Euclides para el cálculo del MCD

Este programa en Python muestra una forma visual y didáctica de cómo funciona el **algoritmo de Euclides** para calcular el **Máximo Común Divisor (MCD)** de dos números enteros.

---

## Descripción

El algoritmo de Euclides es un método eficiente para encontrar el MCD entre dos números. Se basa en la propiedad de que el MCD de dos números \( m \) y \( d \) es el mismo que el MCD entre \( d \) y el residuo \( r \) de la división de \( m \) entre \( d \).

Este programa:

- Solicita al usuario que ingrese dos números enteros.
- Calcula el MCD utilizando el algoritmo de Euclides.
- Muestra paso a paso cómo se realiza la división y el cálculo del residuo en cada iteración.
- Al final, imprime el resultado final del MCD.

---

## Código principal

```python
def mcd(m, d):
    if m < d:
        m, d = d, m
    while d != 0:
        q = m // d
        r = m % d
        print(f"MCD({m}, {d}): {m} = {q} × {d} + {r}")
        m, d = d, r
    return m
