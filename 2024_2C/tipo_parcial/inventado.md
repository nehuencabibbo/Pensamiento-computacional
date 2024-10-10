# Estadisticas 

**OBS:** Un benchmark es un resultado porcentaje entre 0 y 100 que representa a duras penas que tan bueno es un modelo en un determinado area.

Con el auge actual de la inteligencia artificial, una empresa quiere contratar un servicio de pago para que los trabajadores de la empresa tengan acceso a la mejor version de uno de los modelos del momento, y así aumentar la productividad de sus trabajadores.

Para esto, la empresa fue recompilando información sobre los benchmarks de los distintos modelos en los que estaba interesada. Dado que se necesitan inversiones, a veces las compañias que propoporcionan estos modelos mienten respecto a los benchmarks de los mismos.

Se nos pide hacer un analisis acerca de la información recompliada, y obtener el promedio de los benchmarks del mejor y peor modelo, el nombre del peor y mejor modelo.

Se considera que un benchmark es probablemente falso si es mayor a 90.0. Y **no** se lo debe tener en cuenta a la hora de hacer el promedio de los benchmarks.

Hacer una funcion que reciba una lista de tuplas como la del ejemplo siguiente y calcule las estadisticas pedidas anteriormente.

Ejemplo:

```py
benchmarks = [
    ("o1", (80.1, 70.2, 19.2)), 
    ("claude-3.5", (60.2, 5.2, 30.2)), 
    ("LLaMa-3", (60.5, 55.3, 40.0))
]

obtener_estadisticas(benchmarks)
```

debe devolver:

```py
('LLaMa-3', 51.93333333333334, 'claude-3.5', 31.86666666666667, 1)
```

**OBS:** Asumir que siempre, para cada modelo, va a haber al menos un benchmark que sea menor a 80.0