def es_divisible_por(a, b):
    return a % b == 0

def es_primo(numero):
    for i in range(2, numero // 2):
        if es_divisible_por(numero, i):
            return False 
        
    return True
    

numero = 49979687 
print(es_primo(numero))