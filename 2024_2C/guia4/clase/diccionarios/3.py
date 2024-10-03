# 1 - N veces tengo que simular una tirada e ir 
# contando las aparicion del valor en un diccionario

# tiradas = 2
# 5
# 6 

# Devuelve: {6: 1, 5: 1}

# tiradas = 2 

# 6
# 6 

# Devuelve: {6: 2}

import random 

def simular_dado(n):
    resultados = {} # valor_tirada: veces_que_salio
    for i in range(n):
        tirada_1 = random.randint(1, 6)
        tirada_2 = random.randint(1, 6)

        suma = tirada_1 + tirada_2
        
        if suma in resultados: 
            resultados[suma] += 1
        else: 
            resultados[suma] = 1

        # Otra forma: 
        # resultados[tirada] = resultados.get(tirada, 0) + 1

    return resultados 

print(simular_dado(2))

# 1 - N veces simular dos tiradas 

# tiradas = 2 

# 4, 2 
# 3, 5

# Devuelve: {6: 1, 8: 1}