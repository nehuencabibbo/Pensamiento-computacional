# Desafío (obligatorio): Laura tiene una lista de diccionarios donde guarda el valor 
# de todas las reviews laborales anuales que le hicieron. La información de cada una 
# es año, seniority en ese momento (trainee, junior, semisenior, senior), el sueldo en 
# ese momento y el valor del bono de performance que le dieron. La semana pasada le avisaron 
# que por políticas de la empresa, los bonos ahora deben calcularse como un porcentaje de su
#  sueldo.

# Laura quiere entonces actualizar sus diccionarios, para que en vez de guardar el 
# monto exacto del bono, guarde el porcentaje que le corresponde. Ejemplo: si en el
# 2019 su sueldo era de $1.000.000 y el bono que le dieron era de $40.000, el bono fue
# del 4% del sueldo.

# Hacer una función que reciba la lista de diccionarios, y para cada una de las reviews,
# modifique el valor del bono por el porcentaje correspondiente.

# Hacer una función que reciba la lista de diccionarios ya modificada y devuelva los años 
# en los que Laura tuvo un bono mayor al 50% de su sueldo. Restricción: usar filter y map.

# A) Para cada review, nosotros tendriamos que calcular el bono y agregarselo...
# B) Me tengo que quedar solo con las reviews que tienen un bono mayor a 50%
# y luego tendria que obtener solo con los años, es decir, mappeo cada review
# solo a su año 
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

# A) 

def obtener_porcentaje_bono(review):
  return review["bono"] / review["sueldo"] * 100

def arreglar_reviews(lista):
  for elem in lista:
    elem["bono"] = obtener_porcentaje_bono(elem)

arreglar_reviews(reviews)
print(reviews)

# B) 

def bono_mayor_50(review):
  return review["bono"] > 50
 
def obtener_año(review):
  return review["año"]

def obtener_años_bono_mayor_50(lista):
  lista_filtrada = list(filter(bono_mayor_50, lista))
  lista_años = list(map(obtener_año, lista_filtrada))
  return lista_años

print(obtener_años_bono_mayor_50(reviews))