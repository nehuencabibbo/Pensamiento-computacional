# def mostrar_info_paises(paises):
#     for elemento in paises:
#         pais = elemento[0]
#         copas = elemento[1]

#         if pais == "Argentina":
#             pais += "⭐⭐⭐"
            
#         print(f"Pais: {pais} - Copas: {copas}")
        
# paises = [("Argentina", 3), ("España",1), ("Uruguay", 2), ("Francia",2)]

# mostrar_info_paises(paises)

# def contar_paises(paises):
#     total = 0
#     for elemento in paises:
#         pais = elemento[0]
#         copas = elemento[1]

#         total += copas

#     return total


# paises = [("Argentina", 3), ("España",1), ("Uruguay", 2), ("Francia",2)]

# print(contar_paises(paises))

# def criterio_de_ordenamiento(datos_pais):
#     pais = datos_pais[0]
#     copas = datos_pais[1]

#     return copas 

# def ordenar_por_copas(paises):
#     return sorted(paises, key=criterio_de_ordenamiento, reverse=True)

# paises = [("Argentina", 3), ("España",1), ("Uruguay", 2), ("Francia",2)]

# paises_ordenados = ordenar_por_copas(paises)
# print(paises_ordenados)