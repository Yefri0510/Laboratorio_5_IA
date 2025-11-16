import random

# Definimos 6 personas (0 a 5)
personas = [0, 1, 2, 3, 4, 5]

# Matriz de satisfacción: satisfaccion[A][B] = puntos que A gana por sentarse junto a B
# Es asimétrica (a 0 le puede gustar 1, pero a 1 puede no gustarle 0)
# (Esto es solo un ejemplo, puedes cambiar los valores a preferencia)
satisfaccion = [
    [0, 5, 1, 8, 2, 3],  # Satisfacción de la Persona 0 con (0, 1, 2, 3, 4, 5)
    [5, 0, 6, 2, 7, 1],  # Satisfacción de la Persona 1 con (0, 1, 2, 3, 4, 5)
    [1, 6, 0, 5, 2, 4],  # Satisfacción de la Persona 2 con (0, 1, 2, 3, 4, 5)
    [8, 2, 5, 0, 6, 9],  # Satisfacción de la Persona 3 con (0, 1, 2, 3, 4, 5)
    [2, 7, 2, 6, 0, 4],  # Satisfacción de la Persona 4 con (0, 1, 2, 3, 4, 5)
    [3, 1, 4, 9, 4, 0]   # Satisfacción de la Persona 5 con (0, 1, 2, 3, 4, 5)
]

def calcular_satisfaccion_total(orden):
    """Calcula la satisfacción total de una disposición de sillas en fila."""
    total = 0
    # Iteramos por todas las sillas excepto la última
    for i in range(len(orden) - 1):
        p1 = orden[i]
        p2 = orden[i+1]
        
        # Sumamos la satisfacción en ambas direcciones
        total += satisfaccion[p1][p2]
        total += satisfaccion[p2][p1]
    return total

def obtener_mejor_vecino(orden_actual):
    """Encuentra el mejor "vecino" intercambiando a dos personas."""
    mejor_orden = list(orden_actual)
    mejor_satisfaccion = calcular_satisfaccion_total(mejor_orden)
    
    # Probamos todos los posibles intercambios (i, j)
    for i in range(len(orden_actual)):
        for j in range(i + 1, len(orden_actual)):
            
            # Creamos una copia y hacemos el intercambio
            orden_vecino = list(orden_actual)
            orden_vecino[i], orden_vecino[j] = orden_vecino[j], orden_vecino[i]
            
            satisfaccion_vecino = calcular_satisfaccion_total(orden_vecino)
            
            # Si este vecino es mejor, lo guardamos
            if satisfaccion_vecino > mejor_satisfaccion:
                mejor_satisfaccion = satisfaccion_vecino
                mejor_orden = orden_vecino
                
    return mejor_orden, mejor_satisfaccion

def hill_climbing():
    """Ejecuta el algoritmo de Hill Climbing."""
    
    # 1. Empezar con una solución aleatoria
    orden_actual = list(personas)
    random.shuffle(orden_actual)
    satisfaccion_actual = calcular_satisfaccion_total(orden_actual)
    
    print(f"Disposición inicial: {orden_actual} (Satisfacción: {satisfaccion_actual})")
    
    while True:
        # 2. Buscar el mejor vecino
        mejor_vecino, satisfaccion_vecino = obtener_mejor_vecino(orden_actual)
        
        # 3. Comparar
        if satisfaccion_vecino > satisfaccion_actual:
            # 4. Moverse al mejor vecino
            print(f"Mejora encontrada:   {mejor_vecino} (Satisfacción: {satisfaccion_vecino})")
            orden_actual = mejor_vecino
            satisfaccion_actual = satisfaccion_vecino
        else:
            # 5. No hay mejoras, hemos llegado a un pico (máximo local)
            print("\nNo se encontraron más mejoras.")
            break
            
    print(f"Disposición final (Máximo Local): {orden_actual}")
    print(f"Satisfacción Total: {satisfaccion_actual}")

# Ejecutar el algoritmo
hill_climbing()