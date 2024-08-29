# Desafío (obligatorio): Laura tiene una lista de diccionarios donde guarda el valor 
# de todas las reviews laborales anuales que le hicieron. La información de 
# cada una es año, seniority en ese momento (trainee, junior, semisenior, senior),
# el sueldo en ese momento y el valor del bono de performance que le dieron. 
# La semana pasada le avisaron que por políticas de la empresa, los bonos ahora deben 
# calcularse como un porcentaje de su sueldo.

# Laura quiere entonces actualizar sus diccionarios, para que en vez de guardar el 
# monto exacto del bono, guarde el porcentaje que le corresponde. Ejemplo: si en el 
# 2019 su sueldo era de $1.000.000 y el bono que le dieron era de $40.000, el bono fue 
# del 4% del sueldo.


# a)
# Hacer una función que reciba la lista de diccionarios, 
# y para cada una de las reviews, modifique el valor del 
# bono por el porcentaje correspondiente.

# b)
# Hacer una función que reciba la lista de diccionarios ya modificada y devuelva 
# los años en los que Laura tuvo un bono mayor al 50% de su sueldo. Restricción: 
# usar filter y map.

reviews = [{
  "año": 2015,
  "seniority": "trainee",
  "sueldo": 10000,
  "bono": 5010
}, {
  "año": 2015,
  "seniority": "trainee",
  "sueldo": 10200,
  "bono": 2550
}, {
  "año": 2015,
  "seniority": "trainee",
  "sueldo": 12300,
  "bono": 2050
}]


#A)
# def reemplazar_bono_por_porcentaje(reviews):
#     for review_laboral in reviews:
#         review_laboral["bono"] = porcentaje_de_sueldo

#Calculo el porcentaje de sueldo dsps con regla de 3
def reemplazar_bono_por_porcentaje(reviews):
    for review_laboral in reviews:
        porcentaje_de_sueldo = review_laboral["bono"] * 100 / review_laboral["sueldo"]
        review_laboral["bono"] = porcentaje_de_sueldo
    
#Esto anda, porque las listas se modifican por referencia, por lo tanto estoy modificando
#cada elemento de la lista original

#**PARA CADA ELEMENTO** yo estoy aplicando una determinada operacion, esto es simplemente
#un map, habria que reescribir la funcion

#El item que modifique se retorna, porque asi lo indica la funcion map (crea una nueva
#lista map, va recolectando los resultados)
def bono_por_porcentaje(review_laboral):
    porcentaje_de_sueldo = review_laboral["bono"] * 100 / review_laboral["sueldo"]
    review_laboral["bono"] = porcentaje_de_sueldo

    return review_laboral
    

reviews = list(map(bono_por_porcentaje, reviews))

print(f"Reviews mappeadas: {reviews}\n")

# B)

#Queremos filtrar (es decir quedarnos) con los anios en los que laura obutvo un
#bono mayor al 50%

#reviews_filtradas = list(filter("?", reviews))

# Que funcion le tengo que pasar?

def filtrar_bono_mayor_a_50_porciento(review_laboral):
    return review_laboral["bono"] > 50

reviews_filtradas = list(filter(filtrar_bono_mayor_a_50_porciento, reviews))

print(f"Reviews filtradas: {reviews_filtradas}")


