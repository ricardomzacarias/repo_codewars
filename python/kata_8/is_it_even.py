"""
In this Kata we are passing a number (n) into a function.

Your code will determine if the number passed is even (or not).

The function needs to return either a true or false.

Numbers may be positive or negative, integers or floats.

Floats with decimal part non equal to zero are considered UNeven for this kata.
"""

# Define la funcion si es par o impar
def is_even(n):
# consultamos si el valor es un integer
    if isinstance(n, int):
# si el resto es igual que 0 es par y retornamos True
        if n%2==0:
            return True
# en este challenge se nos pide evaluar, si es float es directamente "False"
    elif isinstance(n, float):
# evaluamos si es par retornamos false
        if n%2==0:
            return False
# para el resto de valores podemos retornar un false, ya que no pasar cadenas de caracteres
    else:
        return False

# BEST KATA
def is_eve(n):
    return n%2==0
