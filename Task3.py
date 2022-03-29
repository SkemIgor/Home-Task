import itertools

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена',
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

rez = ((tutor, klass) for tutor, klass in itertools.zip_longest(tutors, klasses) if tutor is not None)

print(next(rez))
print(next(rez))
print(next(rez))
print(next(rez))
print(next(rez))
print(next(rez))
print(next(rez))
print(next(rez))
