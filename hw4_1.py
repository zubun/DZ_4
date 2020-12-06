from sys import argv
def zp(productivity, rate, prize):
    salary = int(productivity) * int(rate) + int(prize)
    return salary

script_name, productivity, rate, prize = argv

# print(f"Имя скрипта:", script_name)
# print(f"При выработке в:", productivity)
# print(f"При ставке в:", rate)
# print(f"При премии в:", prize)


print(f"Имя скрипта: {script_name}")
print(f"При выработке в: {productivity}.")
print(f"При ставке в: {rate}.")
print(f"При премии в: {prize}.")
print(f"Ваша зарплата составит : {zp(productivity, rate, prize)}.")