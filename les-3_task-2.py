def num_translate_adv(number):
    """
    Translates numerals from 0 to 10 from English to Russian.
    """
    dict_of_words = {
    'null': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
    }
    if number.istitle():
        number = number.lower()
        uppercase = dict_of_words.get(number)
        print(uppercase.capitalize())

    else:
        print(dict_of_words.get(number))

num_translate_adv('Nine')
num_translate_adv('six')
num_translate_adv('восемь')