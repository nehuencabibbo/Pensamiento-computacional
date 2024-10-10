def obtener_estadisticas(benchmarks_modelos):
    nombre_mejor_modelo = None
    nombre_peor_modelo = None 

    promedio_mejor_modelo = -1
    promedio_peor_modelo = 101
    for modelo, benchmarks in benchmarks_modelos:
        # Tengo que hacer el promedio a mano para descartar los mayores a 
        # 80
        total = 0 
        no_tenido_en_cuenta = 0
        for benchmark in benchmarks:
            if benchmark > 90.0:
                no_tenido_en_cuenta += 1
            else:    
                total += benchmark

        # El promedio es el total sin tener en cuenta los mayores a 80 dividido
        # la cantidad que fue menor a 80 
        # OBS: No olvidarse los parentesis en la resta
        promedio = total / (len(benchmarks) - no_tenido_en_cuenta)

        if promedio > promedio_mejor_modelo:
            promedio_mejor_modelo = promedio
            nombre_mejor_modelo = modelo
        
        if promedio < promedio_peor_modelo:
            promedio_peor_modelo = promedio
            nombre_peor_modelo = modelo

    return nombre_mejor_modelo, promedio_mejor_modelo, nombre_peor_modelo, promedio_peor_modelo


benchmarks = [
    ("o1", (80.1, 70.2, 19.2)), 
    ("claude-3.5", (60.2, 5.2, 30.2)), 
    ("LLaMa-3", (60.5, 55.3, 40.0))
]

print(obtener_estadisticas(benchmarks))