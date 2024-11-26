############################################################
##################### kata_8 ###############################
############################################################
"""
In this Kata we are passing a number (n) into a function.
Your code will determine if the number passed is even (or not).
The function needs to return either a true or false.
Numbers may be positive or negative, integers or floats.
Floats with decimal part non equal to zero are considered UNeven for this kata.
"""
# # Define la funcion si es par o impar
# def is_even(n):
# # consultamos si el valor es un integer
#     if isinstance(n, int):
# # si el resto es mayor que 0 es par y retornamos True
#         if n%2==0:
#             return True
# # en este challenge se nos pide evaluar si es float, es directamente "False"
#     elif isinstance(n, float):
# # evaluamos si es par retornamos false
#         if n%2==0:
#             return False
# # para el resto de valores podemos retornar un false, ya que no pasar cadenas de caracteres
#     else:
#         return False

############################################################
##################### BEST_KATA ############################
############################################################

# # BEST KATA
# def is_eve(n):
#     return n%2==0

############################################################
##################### kata_5 ###############################
############################################################
"""
Pete likes to bake some cakes. 
He has some recipes and ingredients. 
Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""

# # Variables
# recipient={"flour": 500,  "sugar": 200, "eggs": 1}
# available={"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

# # creamos una funcion con dos diccionarios 
# def cakes(recipient: dict,available: dict) -> int:
# # nueva lista para entregar el entero que pide el challenge
#     new_list: list =[]
# # Iteramos keys e indices para evaluarlos
#     for I,Y in enumerate(recipient.keys()):
#         if Y in available.keys():
# # dividimos para obtener la cantidad de "cakes" que pueden realizar
#             new_list.append(int(available[Y]/recipient[Y]))
# # organizamos de menor a mayor para obtener la cantidad de "cakes" a realizar
#             new_list.sort()
#         else:
# # en caso de no cumplir la condicion retornamos 0, que es lo que pide el challenge
#             return 0 
# # retorna el entero que necesita el challenge para concluir
#     return new_list[0]

# cakes(recipient,available)

############################################################
##################### BEST_KATA ############################
############################################################
# 
# def cakes(recipe, available):
# 	return min(available.get(k, 0)/recipe[k] for k in recipe)

############################################################
##################### kata_x ###############################
############################################################