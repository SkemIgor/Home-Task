goods_price = [26.52, 68.84, 17.05, 25.25, 93.16, 39.01, 17.95, 65.02, 51, 56.01, 18.35, 66.66, 25.16, 77.07, 20.22, 13.66]

for i in goods_price:
    rub = int(i)
    kk = float(i - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end = ', ')   # выводим в одну строку
print()                                         # пустой вывод что бы следующий принт не прилипал к предыдущему принту из за end


goods_price = [26.52, 68.84, 17.05, 25.25, 93.16, 39.01, 17.95, 65.02, 51, 56.01, 18.35, 66.66, 25.16, 77.07, 20.22, 13.66]
print(id(goods_price))
goods_price.sort()                     # сортируем по возрастанию
for i in goods_price:
    rub = int(i)
    kk = float(i - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end = ', ')
print()
print(id(goods_price))


goods_price = [26.52, 68.84, 17.05, 25.25, 93.16, 39.01, 17.95, 65.02, 51, 56.01, 18.35, 66.66, 25.16, 77.07, 20.22, 13.66]
price_sort = ''
goods_price.sort(reverse = True)             # сортируем по убыванию
for i in goods_price:
    rub = int(i)
    kk = float(i - rub) * 100
    price_sort += (f'{rub} руб {kk:02.0f} коп, ')

print(price_sort)

goods_price = [26.52, 68.84, 17.05, 25.25, 93.16, 39.01, 17.95, 65.02, 51, 56.01, 18.35, 66.66, 25.16, 77.07, 20.22, 13.66]
goods_price.sort(reverse = True)
print(goods_price[:5])






