# Defectuoso -> 10 o mas tiradas y salen la mitad o menos de los valores posibles


def experimento(tiradas, caras):
    cantidad_de_tiradas = sum(list(tiradas.values())) 
    if cantidad_de_tiradas < 10:
        print("No se puede determinar")
        return

    for (cara, cantidad_de_veces_que_salio) in tiradas.items():
        print(f"La cara {cara} salio {cantidad_de_veces_que_salio}")

    cantidad_de_valores_que_salieron = len(tiradas.keys()) 
    if cantidad_de_valores_que_salieron <= caras / 2:
        print("Esta defectuoso")
    else:
        print("No esta defectuoso")

tiradas = {
    2: 5,
    4: 5,
}

experimento(tiradas, 4)