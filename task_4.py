# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def multiplier(num):
#
#     list_num = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             list_num.append(i)
#     return list_num
#
# num = int(input('Введите натуральное число: '))
# print(multiplier(num))

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# my_list = [62, 15, 62, 14, 1, 12, 4, 1, 2, 3, 12, 8, 7, 6, 5, 6, 4, 3, 21, 2, 1, 123]
# sort_list = []

# Первый вариант

# for i in my_list:
#     count = 0
#     for j in my_list:
#         print(i, j)
#         if i == j:
#             count += 1
#     if count == 1:
#         sort_list.append(i)
# print(sort_list)

# Второй вариант

# for i in my_list:
#     if my_list.count(i) == 1:
#         sort_list.append(i)
# print(sort_list)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# import random
#
# def rdm ():
#     return random.randint(1, 101)
#
#
# def list_numbers(k):
#     list_num = [rdm() for i in range(k)]
#     polynomial = ''
#     while k != 0:
#         if k > 1:
#             polynomial += f'{list_num[k - 1]}*x^{k} + '
#         else:
#             polynomial += f'{list_num[1]}*x + {list_num[0]} = 0'
#         k -= 1
#     return polynomial
#
# k = int(input('Введите степень k: '))
#
# print(list_numbers(k))
#
# with open('polynomial.txt', 'w') as data:
#     data.write(list_numbers(k))