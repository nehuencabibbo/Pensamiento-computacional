# A)

Se pide hacer una funcion, que reciba una lista con numeros entre 1 y 7 y para cada numero en la lista, devuelva el dia de la semana al que corresponde, es decir, para 1 deberia devolver Lunes, para 2 Martes y asi sucesivamente.

Ejemplo: 

```py
obtener_dia_de_la_semana([1, 3, 4, 2])
```

debe devolver: 

```py
> ["Lunes", "Miercoles", "Jueves", "Martes"]
```

# B)

Hacer otra funcion, que reciba el resultado de la anterior, y devuelva solo los dias que comienzan con la letra M. Por ejemplo:

```py
dias = ["Lunes", "Miercoles", "Jueves", "Martes"]
obtener_dias_que_comienzan_por(dias)
```

debe devolver: 

```py
> ["Miercoles", "Martes"]
```

**OBS (para mi):** Si se quiere hacer generico para la letra y filter se tiene que pasar un closure que lalme a la funcion de filtro i.e filter(lambda dia: filtrar(dia, args...), ...)