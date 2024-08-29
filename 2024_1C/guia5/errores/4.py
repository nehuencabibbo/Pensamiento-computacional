def clima(archivo):
    with open(archivo, "r") as a:
        lineas = a.readlines()
        cantidad_total_de_valores = len(lineas)
        valores_invalidos = 0
        total = 0
        for linea in lineas:
            try:
                numero = float(linea.strip("\n"))
                total += numero
            except ValueError:
                valores_invalidos += 1
        
        return total / cantidad_total_de_valores, valores_invalidos / cantidad_total_de_valores * 100
    
