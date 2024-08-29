def es_primo(num):
  for i in range(2, num):
    if num % i == 0:
      return False 
    
  return True

es_primo(49979687)