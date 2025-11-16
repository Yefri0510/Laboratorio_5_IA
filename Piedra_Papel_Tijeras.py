import random

def jugar_piedra_papel_tijera_optimo():
    """
    Decide la jugada óptima asumiendo un oponente racional.
    La estrategia óptima es un "equilibrio de Nash" de estrategia mixta.
    """
    opciones = ['piedra', 'papel', 'tijera']
    
    # La estrategia óptima (in-explotable) es elegir una al azar
    # con igual probabilidad (1/3 para cada una).
    
    jugada = random.choice(opciones)
    return jugada

# --- Ejecución ---
print("Simulando 10 jugadas óptimas contra un oponente racional:")

for i in range(10):
    print(f"Jugada {i+1}: {jugar_piedra_papel_tijera_optimo()}")

print("\n¿Qué estrategia adopta el algoritmo?")
print("Adopta una 'estrategia mixta' aleatoria.")
print("Sabe que cualquier jugada predecible (como 'jugar siempre piedra')")
print("será explotada por un oponente racional. Por lo tanto, la única")
print("jugada 'óptima' es ser impredecible.")

