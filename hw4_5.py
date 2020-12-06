from functools import reduce


def multiplication_function(prev_el, el):
    return prev_el * el

even_numbered = [el for el in range(100, 1001) if el % 2 == 0 ]
print(even_numbered)
print(reduce(multiplication_function,even_numbered))