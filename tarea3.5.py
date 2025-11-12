import random

#personas de la aldea
grupo = ["V"]*50 + ["M"]*30 + ["R"]*20

def simulacion(intentos=300000):
    exitos = 0
    for i in range(intentos):
        seleccion = random.sample(grupo, 30)
        
        v = 0
        m = 0
        r = 0
        for persona in seleccion:
            if persona == "V":
                v += 1
            elif persona == "M":
                m += 1
            else:
                r += 1
        
        if v == 10 and m == 10 and r == 10:
            exitos += 1
    
    return exitos / intentos

#simulo 
prob = simulacion(1000000)  #con un millon de intentos
print("Probabilidad aprox:", prob)

# Nota: 7.0
