def thesaurus(*args):
    directory = {}
    for letter in args:

        directory[letter[0]] = directory.setdefault(letter[0], []) + [letter]
    directory = sorted(directory.items())
    print(dict(directory))

thesaurus('Вася', 'Петр', 'Игорь', 'Ирина', 'Абрам', 'Валера', 'Дмитрий', 'Полина', 'Света', 'Максим', 'Лео', 'Леонид', 'Люся')