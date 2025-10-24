import numpy as np
import time
from scipy.optimize import newton

#la funcion y su derivada
def f(x):
    return x - np.cos(x)

def f_prima(x):
    return 1 + np.sin(x)

#parametro
x_inicial = 0.5
tolerancia = 1e-8
max_iter = 50
repeticiones = 10000

#metodo de newto aplicado directamente
inicio = time.perf_counter()
for _ in range(repeticiones):
    x = x_inicial
    for _ in range(max_iter):
        fx = f(x)
        fpx = f_prima(x)
        if abs(fpx) < 1e-12:
            break
        x_nuevo = x - fx / fpx
        if abs(x_nuevo - x) < tolerancia:
            break
        x = x_nuevo
    raiz_propia = x
fin = time.perf_counter()
t_propio = (fin - inicio) / repeticiones

# scipy
inicio = time.perf_counter()
for _ in range(repeticiones):
    raiz_scipy = newton(f, x_inicial, fprime=f_prima, tol=tolerancia, maxiter=max_iter)
fin = time.perf_counter()
t_scipy = (fin - inicio) / repeticiones

#comparacion

print(f"Raíz (método propio): {raiz_propia}")
print(f"Raíz (SciPy):         {raiz_scipy}")
print("tiempos promedio por ejecucion:")
print(f"Propio: {t_propio:.10f} s")
print(f"SciPy:  {t_scipy:.10f} s")

if t_scipy < t_propio:
    print(f"SciPy fue {t_propio / t_scipy:.2f} veces más rápido.")
else:
    print("mi metodo fue mas rapido.")

# Nota: 7.0
