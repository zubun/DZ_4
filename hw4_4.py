from random import randint
def repetition(list):
    without_repeating_list = []
    list_2 = [without_repeating_list.append(el) for el in list if el not in without_repeating_list]
    return without_repeating_list

list_1 = [randint(0,10) for el in range(15)]
print(f"Исходный список: {list_1}.")
print(f"Результат: {repetition(list_1)}.")
