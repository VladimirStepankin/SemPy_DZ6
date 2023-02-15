n = int(input("Введите количество элементов массива: "))
list_1 = list()
from random import randint
for i in range(n):
    list_1.append(randint(0, 100))
print(list_1)
print()
list_2 = list()
min_number = int(input("Введите минимальное значение "))
max_number = int(input("Введите максимальное значение "))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        list_2.append(i)
print(list_2)
