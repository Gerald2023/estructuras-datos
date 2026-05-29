import time


# =========================
# Algoritmo 1
# =========================
def algoritmo1(n): 

    contador = 0            # O(1) dura 1
    suma = 0                # O(1) dura 1

    # Operaciones constantes    
    a = 5                       # O(1) esto dura 1
    b = 7                       # O(1) esto dura 1
    c = a * b                   # O(1) esto dura 1

                 #aca tenemos 5 en total 

    for i in range(n):          # se repite n veces

        for j in range(n):      # se repite n veces 


            contador += 1       # O(1) esto dura 1

            suma += i + j       # O(1) esto dura 1

            x = i * j           # O(1) esto dura 1
            y = x + 100         # O(1) esto dura 1
            z = y / 3           # O(1) esto dura 1

            if x % 2 == 0:      # O(1) esto dura 1
                suma += 1       # O(1) esto dura 1
            else:
                suma -= 1       # O(1) esto dura 1

    promedio = suma / (n * n)    # esto dura 1

    return contador + promedio    # O(1) esto dura 1  

                            #aca tenemos 2 en total
#MI analisis para big O:
#1+1+1+1+1+1+1+1 = 8
#se repite n veces:  8 * n * n = 8n²
#Tenia al inicia 5
#Tenia al final 2
#En total : 8n² + 7
#Resultado : O(n²)


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

medir_tiempo(algoritmo1, n)