nombres = ['Agustina', 'Iara', 'Priscila', 'Sol', 'Lucía']
cupo = 3

nombres[cupo:len(nombres)]

no_entraron = []
for i in range(3, len(nombres)):
    no_entraron.append(nombres[i])