s = input("Введите текст для кодировки: ")
with open('cod.txt', 'w', encoding='utf-8') as data:
    data.write(s)

def coding(data = 'cod.txt'):
    res = ''
    count = 1

    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            count += 1
        else:
            res = res + str(count) + data[i]
            count = 1
    if count > 1 or (data[len(data)-2] != data[-1]):
        res = res + str(count) + data[-1]

    with open('coding.txt', 'w', encoding='utf-8') as coding:
        coding.write(res)

    return res



def decoding(txt = 'coding.txt'):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''

    with open('decoding.txt', 'w', encoding='utf-8') as decoding:
        decoding.write(res)

    return res


print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")