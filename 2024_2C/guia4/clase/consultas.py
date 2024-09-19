lista_generica = [
    ("a", (90, 50)), 
    ("b", (5, 20))
]

for elemento in lista_generica:
    modelo = elemento[0]
    benchmarks = elemento[1]

    total = 0
    no_tenidos_en_cuenta = 0
    for bench in benchmarks: 
        if bench < 90.0:
            total += bench
        else:
            no_tenidos_en_cuenta += 1


