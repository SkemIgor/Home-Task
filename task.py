# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# num = input('Введите число: ')
# sum = 0
# for i in num:
#     sum += int(i)
# print(sum)

# 1. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# x = True
# while x:
#     num = int(input('Введите положительное число: '))
#     if int(num) < 1:
#         x = True
#     else:
#         prz = []
#         count = 1
#         while count != num + 1:
#             if len(prz) == 0:
#                 prz.append(1)
#             else:
#                 prz.append(count * prz[len(prz) - 1])
#             count += 1
#         print(prz)
#         break

# 1. Реализуйте алгоритм перемешивания списка.
# import random
#
# lst = [1, 10, 100, 1000, 2000, 3000, 4000, 5000, 6000]
#
# random.shuffle(lst)
# print(lst)