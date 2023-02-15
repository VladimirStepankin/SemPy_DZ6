a1 = int(input("Введите первый член прогрессии "))
d = int(input("Введите разность "))
n = int(input("Введите количество членов прогрессии "))
list1 = list()
for i in range(n):
    An = a1 + i*d
    list1.append(An)
print(list1)