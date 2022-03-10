def num_translate(number):
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
    print(dict_of_words.get(number))

num_translate('ten')
num_translate('twen')