def ingresar_fichas(fichas):
    while fichas > 0:
        ingreso = input("Ingresa {} fichas para comenzar: ".format(fichas))
        if ingreso == "F":
            fichas -= 1

ingresar_fichas(2)

#8a
def maquina_de_juguetes(n):
    while n > 0:
        variable = str(input("Ingresa 3 fichas para comenzar:"))
        if variable.upper() == "F":
            n -= 1
        
  
maquina_de_juguetes(3)
