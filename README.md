# Laboratorio 5

* Yefri Stiven Barrero Solano - 2320392
* Jose Alejandro Mesa Chaves - 2291048
* Juan Dvid Becerra Pulido - 2283133

## 1\. Organizando Sillas (Hill Climbing)

Este problema utiliza un algoritmo de **Búsqueda Local** (Local Search) conocido como **Hill Climbing** (Ascenso de Colina) para encontrar una buena disposición de 6 personas en 6 sillas, maximizando la "satisfacción" total.

### Fundamentación Conceptual

El Hill Climbing es una **heurística de optimización**. Su filosofía es simple:

1.  Empezar en un estado aleatorio (una disposición de sillas al azar).
2.  Evaluar la "calidad" de ese estado (calcular la satisfacción total).
3.  Explorar todos los "vecinos" inmediatos (en nuestro caso, todas las posibles parejas que se pueden intercambiar de sitio).
4.  Si un vecino tiene una calidad *mejor* que el estado actual, moverse a ese estado.
5.  Repetir el proceso hasta que no exista ningún vecino mejor.

### El "Máximo Local"

El objetivo clave de este ejercicio es demostrar el concepto de **máximo local**.

  * Un **Máximo Global** es la *mejor solución posible* que existe.
  * Un **Máximo Local** es una solución que es *mejor que todos sus vecinos*, pero no necesariamente la mejor de todas.

El algoritmo de Hill Climbing, por su naturaleza, siempre se detendrá en el primer "pico" que encuentre. Es como escalar una montaña en medio de una niebla densa: solo puedes saber si el paso siguiente es hacia arriba o hacia abajo. Una vez que llegas a un punto donde todos los pasos a tu alrededor son hacia abajo, te detienes, asumiendo que estás en la cima.

Es posible que esta "cima" (máximo local) sea solo una pequeña colina, y que el verdadero "Everest" (máximo global) esté en otra parte.

### Implementación Clave

La lógica central del algoritmo se encuentra en el bucle principal, que busca continuamente un "vecino" (un intercambio de dos personas) que mejore la puntuación actual. Si no encuentra ninguno, termina.

```python
def hill_climbing():
    # 1. Empezar con una solución aleatoria
    orden_actual = [...]
    satisfaccion_actual = calcular_satisfaccion_total(orden_actual)
    
    while True:
        # 2. Buscar el mejor vecino (intercambiando dos personas)
        mejor_vecino, satisfaccion_vecino = obtener_mejor_vecino(orden_actual)
        
        # 3. Comparar
        if satisfaccion_vecino > satisfaccion_actual:
            # 4. Moverse al mejor vecino
            orden_actual = mejor_vecino
            satisfaccion_actual = satisfaccion_vecino
        else:
            # 5. No hay mejoras: Hemos llegado a un Máximo Local
            break
```

## 2\. Problema del Cambio de Monedas (Algoritmo Voraz)

Este problema implementa un **Algoritmo Voraz** (Greedy Algorithm) para resolver el problema del cambio: dar $63 usando el menor número de monedas posible (con denominaciones de 50, 20, 10, 5 y 1).

### Fundamentación Conceptual

Un algoritmo voraz es aquel que, en cada paso, toma la decisión que parece **localmente óptima** en ese momento, sin considerar las consecuencias futuras.

Para el problema del cambio, la estrategia voraz es:
"En cada paso, tomar la moneda de **mayor valor posible** que no exceda el monto restante."

El algoritmo hace esto repetidamente hasta que el monto restante es cero.

### ¿Es Óptimo?

El objetivo de este ejercicio es analizar la estrategia "siempre toma lo mejor ahora".

En este caso particular (dar $63 con monedas [50, 20, 10, 5, 1]), la estrategia voraz *sí* produce la solución óptima (la que usa el menor número de monedas):

1.  Toma **1** de $50 (restan $13)
2.  Toma **1** de $10 (restan $3)
3.  Toma **3** de $1 (restan $0)
    Total: 5 monedas.

> **Importante:** La estrategia voraz no es óptima para *todos* los sistemas de monedas. Por ejemplo, si tuviéramos monedas de [1, 3, 4] y quisiéramos dar $6 de cambio:
>
>   * **Voraz:** 4 + 1 + 1 (3 monedas)
>   * **Óptimo:** 3 + 3 (2 monedas)
>
> Nuestro sistema de monedas [50, 20, 10, 5, 1] se considera "canónico", y para él, la estrategia voraz siempre funciona.

A diferencia del problema de Piedra, Papel o Tijera, este problema *no es adversarial*. No hay un "oponente"; es un problema de optimización puro.

### Implementación Clave

El núcleo del algoritmo es un simple bucle que itera sobre las monedas (ordenadas de mayor a menor) y "consume" tanto como puede de cada una.

```python
def dar_cambio_voraz(monto, monedas):
    monedas.sort(reverse=True)
    cambio_dado = {}
    
    for moneda in monedas:
        if monto <= 0:
            break
        
        # 1. Decisión Voraz: ¿Cuántas caben?
        cantidad_monedas = monto // moneda
        
        if cantidad_monedas > 0:
            # 2. Tomar la decisión
            cambio_dado[moneda] = cantidad_monedas
            
            # 3. Reducir el problema
            monto -= moneda * cantidad_monedas
            
    return cambio_dado
```

## 3\. Juego de Piedra, Papel o Tijera (Teoría de Juegos)

Este problema aborda la estrategia óptima en un juego de suma cero contra un oponente racional.

### Fundamentación Conceptual

Este ejercicio demuestra por qué la estrategia "toma lo mejor ahora" (voraz) es **terrible** en un entorno competitivo.

1.  **El Fracaso de la Estrategia Voraz:** Si intentas jugar "lo mejor", ¿qué sería? Si asumes que tu oponente jugará "Piedra", tu jugada voraz es "Papel".
2.  **El Oponente Racional:** Pero el oponente es racional. Él *sabe* que tú vas a jugar "Papel" para ganarle a su "Piedra", así que él no jugará "Piedra". Él jugará "Tijera" para ganarle a tu "Papel".
3.  **La Paradoja:** Pero tú también eres racional, y sabes que él sabe... esto crea un bucle infinito.

Cualquier estrategia determinista (ej. "jugar siempre Piedra") es predecible y, por lo tanto, explotable.

### La Solución: Equilibrio de Nash

La única estrategia "óptima" en este juego es **no ser predecible**. Esto se conoce como **Equilibrio de Nash** de estrategia mixta.

La estrategia óptima es jugar:

  * Piedra con 1/3 de probabilidad.
  * Papel con 1/3 de probabilidad.
  * Tijera con 1/3 de probabilidad.

De esta manera, tu estrategia es **in-explotable**. No importa lo que haga tu oponente (incluso si puede leer tu mente o tu código), no puede encontrar una estrategia que le garantice una victoria sistemática contra ti. A largo plazo, lo mejor que puede esperar es empatar.

### Implementación Clave

La implementación de esta compleja teoría es, paradójicamente, la más simple de todas: elegir una opción al azar.

```python
import random

def jugar_piedra_papel_tijera_optimo():
    """
    Decide la jugada óptima (in-explotable) 
    usando un Equilibrio de Nash.
    """
    opciones = ['piedra', 'papel', 'tijera']
    
    # La estrategia óptima es una distribución de probabilidad uniforme
    jugada = random.choice(opciones)
    return jugada
```
