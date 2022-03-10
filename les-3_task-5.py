import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def jokes(n):

    for i in range(n):
        joke = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
        print(joke)

jokes(3)