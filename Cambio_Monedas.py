def dar_cambio_voraz(monto, monedas):
    """
    Calcula el cambio usando un algoritmo voraz.
    Las monedas deben estar ordenadas de mayor a menor.
    """
    
    # Ordenamos por si acaso, de mayor a menor
    monedas.sort(reverse=True)
    
    cambio_dado = {}
    
    print(f"Calculando cambio para: ${monto}")
    
    for moneda in monedas:
        if monto <= 0:
            break  # Ya terminamos de dar cambio
        
        # 1. Decisión Voraz: ¿Cuántas monedas de este valor caben?
        cantidad_monedas = monto // moneda
        
        if cantidad_monedas > 0:
            # 2. Tomar la decisión
            cambio_dado[moneda] = cantidad_monedas
            
            # 3. Reducir el problema
            monto_restado = moneda * cantidad_monedas
            monto -= monto_restado
            
            print(f"  - Se dieron {cantidad_monedas} moneda(s) de ${moneda}. (Resta: ${monto})")
            
    return cambio_dado

# --- Ejecución ---
monto_total = 63
monedas_disponibles = [50, 20, 10, 5, 1]

cambio = dar_cambio_voraz(monto_total, monedas_disponibles)

print("\n--- Resultado Final ---")
print(f"Cambio total ({monto_total}): {cambio}")
