import numpy as np
#primera pregunta
# Lista dada
frecuencias = np.array([
    12.53, 1.42, 4.68, 5.86, 13.68, 0.69, 1.01, 0.7,
    6.25, 0.44, 0.02, 4.97, 3.15, 6.71, 0.31, 8.68,
    2.51, 0.88, 6.87, 7.98, 4.63, 3.93, 0.9, 0.01,
    0.22, 0.9, 0.52
])

#Normalizamos
probabilidades = frecuencias / np.sum(frecuencias)

#calculamos la entropia 
entropia = -np.sum(probabilidades * np.log2(probabilidades))

print("La entropía de Shannon del español es:", entropia, )

#segunda pregunta
print("es posible reducirlo debio a que se repite mucho la vocal e, repeticion de prefijos y repeticion de silabas, esto permite que la entropia del mensaje se reduzca  ")

# Nota: 7.0
