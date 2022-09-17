my_str = "абвес Привет. Кабвк делабв проабвесил Как то так! абвгдеж"


def del_word_from_abc(my_str):
    my_text = list(filter(lambda x: 'абв' not in x, my_str.split()))
    my_text = " ".join(my_text)
    return my_text


print(del_word_from_abc(my_str))