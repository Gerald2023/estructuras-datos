import time


# =========================
# Algoritmo 2
# =========================
def algoritmo2(n):

    total = 0                    # esto dura 1
    suma_pares = 0                # esto dura 1
    suma_impares = 0                # esto dura 1

    # Operaciones constantes
    a = 10                    # esto dura 1
    b = 20                    # esto dura 1
    c = a + b                # esto dura 1
            # en total 6
    for i in range(n):        # esto dura n

        total += i            # esto dura 1

        if i % 2 == 0:          # esto dura 1
            suma_pares += i        # esto dura 1
        else:
            suma_impares += i    # esto dura 1

        x = i * 2                # esto dura 1
        y = x + 5            # esto dura 1
        z = y / 2            # esto dura 1
            # En total 7
    
    promedio = total / n   # esto dura 1

    return promedio + suma_pares + suma_impares   # esto dura 1
                            # En total 2

# Mi resultado final :7n + 8 O(n)

# =========================
# Medición de tiempo
# =========================
def medir_tiempo(funcion, n):

    inicio = time.perf_counter()

    resultado = funcion(n)

    fin = time.perf_counter()

    tiempo = fin - inicio

    print(f"\n{funcion.__name__}")
    print(f"n = {n}")
    print(f"Resultado = {resultado}")
    print(f"Tiempo = {tiempo:.8f} segundos")


# =========================
# Programa principal
# =========================

n = int(input("Ingrese el valor de n: "))

medir_tiempo(algoritmo2, n)
