# <p style="text-align:center"> Dados defectuosos </p>

En una fabrica de dados para juegos de mesa se quiere ver si un dado es defectuoso o no. Para ello se han realizado experimentos y se determino que se considera un dado como defectuoso en caso de hacer 10 o mas tiradas y que solo salgan la mitad o menos de los valores posibles. En caso de que las tiradas sean menores a 10, no se puede determinar si el dado esta defectuoso o no.

Nos han pedido que creemos una funcion que dados una cantidad de tiradas para realizar (t) y la cantidad de caras del dado (n), indique si se puede determinar si está defectuoso o no, y en caso de que se pueda determinar, hacerlo.

Se deben mostrar los datos del experimento (t y n), y para todo caso que se pueda determinar si el dado esta defectuoso o no, se debe mostrar por pantalla los resultados del experimento (cuantas veces salio cada cara).

Ejemplo:

```python
experimento(6, 4) #Se hacen 6 tiradas de un dado de 4 caras

#> Cantidad de tiradas: 6 - Cantidad de caras del dado: 4
#> No se puede determinar si esta defectuoso el dado

experimento(10, 4) #Se hacen 10 tiradas de un dado de 4 caras

#> Cantidad de tiradas: 10 - Cantidad de caras del dado: 4
#> La cara 2 salio 5 veces
#> La cara 4 salio 5 veces
#> El dado esta defectuoso

experimento(11, 4) #Se hacen 11 tiradas de un dado de 4 caras

#> Cantidad de tiradas: 11 - Cantidad de caras del dado: 4
#> La cara 3 salio 3 veces
#> La cara 2 salio 6 veces
#> La cara 1 salio 2 veces
#> El dado NO esta defectuoso
```

**OBS**: Si la cantidad de caras es impar, usar division entera para calcular la mitad.

**AYUDA**: Se puede separar la funcionalidad de mostrar los datos por pantalla y la de
tirar el dado:

```python
def simular_tiro_dado(t, n):
    #Hacer algo

def experimento(t, n):
    #Hacer algo

    datos_experimento = simular_tiro_dado(t, n)

    #Hacer algo
```

**BONUS**: Muestren los datos del experimento de menor a mayor segun el numero de cara
