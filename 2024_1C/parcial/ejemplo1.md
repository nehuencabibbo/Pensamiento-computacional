# <p style="text-align:center"> Mejores promedios </p>

Se quiere otorgar los premios al mejor estudiante del CBC este 2024. Para ello, se debe determinar los 3 mejores estudiantes. Los datos de cada alumno estan guardados de la siguiente manera:

```python
[
    {
        nombre
        padron
        año_de_nacimiento
        notas: [materia1, materia2, ..., materiaN]
    },
    ...
]
```

Se quiere crear una funcion, que reciba la lista de informacion de los alumnos, y muestre por pantalla el nombre, padron y promedio de los 3 que tengan mejor promedio, con el siguiente formato, y ordenados descendentemente por promedio:

```python
#>nombre - padron - promedio 
#>nombre - padron - promedio 
#>nombre - padron - promedio 
```

Se deja la siguiente data de ejemplo para que puedan probar su programa:

```python
alumnos = [
    {
        "nombre": "Nehuén",
        "padron": 108025,
        "año_de_nacimiento": 2002,
        "notas": [9, 8, 6, 7, 10, 9],
    },
    {
        "nombre": "Lucas",
        "padron": 108026,
        "año_de_nacimiento": 2001,
        "notas": [8, 7, 9],
    },
    {
        "nombre": "Maria",
        "padron": 108027,
        "año_de_nacimiento": 2000,
        "notas": [10, 9, 8, 10, 9, 8, 4, 5, 6],
    },
    {
        "nombre": "Juan",
        "padron": 108028,
        "año_de_nacimiento": 2003,
        "notas": [7, 8, 10],
    },
    {
        "nombre": "Ana",
        "padron": 108029,
        "año_de_nacimiento": 2004,
        "notas": [9, 8, 9, 8, 9],
    }
]
```

La salida esperada para los datos anteriores es la siguiente:

```python
Ana - 108029 - 8.6
Juan - 108028 - 8.333333333333334
Nehuén - 108025 - 8.166666666666666
```

**PISTA**: Dividir el problema en subproblemas que sepan resolver
