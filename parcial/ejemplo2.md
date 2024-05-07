En una fabrica de dados se quiere ver si un dado es defectuoso o no. Para ello se han realizado experimentos y se determino, que se considera un dado como defectuoso en caso de hacer 10 o mas tiradas del mismo y que salgan solo la mitad o menos de los valores posibles del mismo. En caso de que las tiradas sean menores a 10, no se puede determinar si el dado esta defectuoso o no.

Nos han pedido que creemos una funcion que dados una cantidad de tiradas para realizar (t) y la cantidad de caras del dado (n), indique si se puede determinar si esta defectuoso el dado o no, y en caso de que se pueda determinar, hacerlo. Se deben mostrar los datos del experimento (t y n), y para todo caso que se pueda determinar si el dado esta defectuoso o no, se debe mostrar por pantalla los resultados del mismo (cuantas veces salio cada cara).

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