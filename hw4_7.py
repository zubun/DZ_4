def fact(n):
    for el in range(n + 1):
        if el < 2:
            yield 1
        if el >= 2:
            v = 1
            for q in range(el+1):
                if q == 0:
                    q = 1
                v = v * q
            yield v
number = int(input("Введите число: "))
for el in fact(number):
    print(el)

