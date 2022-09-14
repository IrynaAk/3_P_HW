# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.11, 5, 10.01] => 0.19

a = [1.1, 1.2, 3.11, 5, 10.01]
max_el = a[0] * 100 % 100
min_el = a[0] * 100 % 100

for i in range(int(len(a))):
    e = a[i] * 100 % 100
    if e ==0:
        continue
    if e > max_el:
        max_el = e
    if e < min_el:
        min_el = e
print(round((max_el- min_el)/100,3))


# number = float(input("please type a number: "))
# st = str(number)
# a = list(st)
# h = 0
# for i in range(len(a)):
#     if a[i] == '.':
#         continue
#     h += int(a[i])
# #print(a)
# print(h)




