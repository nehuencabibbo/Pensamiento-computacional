reviews = [{
  "año": 2015,
  "seniority": "trainee",
  "sueldo": 10000,
  "bono": 5010 # 10000 / 5010 * 100
}, {
  "año": 2015,
  "seniority": "trainee",
  "sueldo": 10200,
  "bono": 2550 # 10200 / 2550 * 100
}, {
  "año": 2015,
  "seniority": "trainee",
  "sueldo": 12300,
  "bono": 2050
}]

# review["bono"] = reviews["sueldo"] / review["bono"] * 100


def bono_porcentaje(lista_reviews): 
    for review in lista_reviews: 
        review["bono"] = review["bono"] / review["sueldo"] * 100

bono_porcentaje(reviews)
for review in reviews:
    print(review)
