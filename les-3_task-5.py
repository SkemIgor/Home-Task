import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def jokes(quantity_of_jokes, replays=False):
    """
    returns a joke from 3 lists
    :param quantity_of_jokes:
    :param replays: If True no repeats
    :return:
    """
    copy_joke = []

    for i in range(quantity_of_jokes):

        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjectiv = random.choice(adjectives)

        joke = f'{noun} {adverb} {adjectiv}'
        copy_joke.append(joke)

        if replays:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjectiv)

    print(copy_joke)

jokes(5, True)