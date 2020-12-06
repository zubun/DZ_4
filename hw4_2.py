import random
def more_function(list):
    final_list = []
    final_list_1 = [final_list.append(list[el+1]) for el in range(len(list)-1) if list[el]<list[el+1]]
    return final_list


my_list = [el**2 for el in range(3, 15)]
random.shuffle(my_list)
print(f"Cписок исходных значений: {my_list}")
print(f"Результат : {more_function(my_list)}")







# import random
# def more_function(list):
#     final_list = []
#     for el in range(len(list)-1):
#         if list[el]<list[el+1]:
#             final_list.append(list[el+1])
#     return final_list
#
#
# my_list = [el**2 for el in range(3, 15)]
# random.shuffle(my_list)
# print(f"Cписок исходных значений: {my_list}")
# print(f"Результат : {more_function(my_list)}")