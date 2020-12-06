from itertools import count
from itertools import cycle
''' Итератор, генерирующий целые числа, начиная с указанного, заканчивая указанным'''
def count_list(start, stop):
    list = []
    for el in count(start):
        if el <= stop:
            list.append(el)
        else:
            break
    return list
start = int(input("Введите начальное значение списка(целое число):"))
stop = int(input("Введите конечное значение списка(целое число):"))
print(count_list(start, stop))

'''итератор, повторяющий элементы некоторого списка, определенного заранее.'''
start_1 = input("Введите список:")
stop_1 = int(input("Введите конечное значение списка(целое число):"))

сounters = 0
for el in cycle(start_1):
    if сounters > stop_1:
        break
    print(el)
    сounters += 1