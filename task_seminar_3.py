# ИЗ ПРОШЛОГО ЗАДАНИЯ. Реализуйте алгоритм перемешивания списка.
import random

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
mix_list = []

for i in my_list:
    mix_list.insert(random.randint(0, len(my_list)), i)

print(mix_list)

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

my_list = [4, 8, 15, 16, 23, 42]
res = sum(my_list[1::2])
print(res)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = [4, 8, 15, 16, 23, 42]
my_list2 = []

i = 0
while i < len(my_list) / 2:

	x = my_list[0 + i] * my_list[-1 - i]
	my_list2.append(x)
	i += 1

print(my_list2)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

num = [1.1, 1.2, 3.1, 5, 10.01]
float_list = []
max_num = 0
min_num = 1
i = 0
while i < len(num):
    for k in num:
        k = k % 1
        float_list.append(k)
    for j in float_list:
        if j < min_num:
            min_num = j
        if j > max_num:
            max_num = j
    i += 1

print(max_num - min_num)



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def converter(num):
    """
    converts decimal to binary

    """
    x = ''
    while num > 0:
        if num % 2 == 1:
            x += '1'
        else:
            x += '0'
        num //= 2
    res = x[::-1]
    return res

print(converter(42))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fibonacci(num):
    x = [1, 1]
    for i in range(2, num):
        x.append(x[-1] + x[-2])
    for j in range(-1, num):
        x.insert(0, x[1] - x[0])
    return (x)

print(fibonacci(8))


# 27 Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

s = '1 2 3 4 5 6 7'
if s.isdigit():
    my_list = []
    s = s.split()
    for i in s:
        my_list.append(int(i))
    print(min(my_list), max(my_list))
else:
    print('Введите число')

# 28 Найти корни квадратного уравнения Ax² + Bx + C = 0

def quadratic(a, b, c):
    my_list = []
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = ((-b + d**0.5) / (2 * a))
        my_list.append(x1)
        x2 = ((-b - d**0.5) / (2 * a))
        my_list.append(x2)
        return my_list
    elif d == 0:
        x = -b / (2 * a)
        my_list.append(x)
        return my_list
    else:
        return my_list

res = quadratic(1, 6, 9)

print(res)
