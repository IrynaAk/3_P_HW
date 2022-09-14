# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  

n = 8

def Fibonachi(a):
    if a ==0:
        return 0
    elif a == 1 or a == 2:
        return 1
    else:
        return Fibonachi(a-1) + Fibonachi(a-2)

l = []

for i in range(n+1):
    l.append(Fibonachi(i))

s = []

for i in range(n):
    s.append((-1)**(n-i+1) * Fibonachi(n-i))

print (s+l)




