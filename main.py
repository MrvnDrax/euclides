


# Una forma visual del funcionamiento del algoritmo de euclides #

a = int(input("Ingresa tu primer numero: "))
b = int(input("Ingresa tu segundo numero: "))
 

def mcd(m, d):
    print("-----Listo para ver cómo funciona el algoritmo?, espero que sí!!!-----")
    if m < d:
        m, d = d, m
        print("Recuerda que el numero mayor siempre debe ser la primera entrada")
    while d != 0:
        q = m // d
        r = m % d
        print(f"MCD({m}, {d}): {m} = {q} × {d} + {r}")
        m, d = d, r
    return m

resultado = mcd(a, b)
print(f"El MCD({a}, {b}) = {resultado}")
