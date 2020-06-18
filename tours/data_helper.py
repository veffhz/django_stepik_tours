import random


def random_limit(dictionary, quantity):
    if len(dictionary) < quantity:
        return random.sample(dictionary.items(), len(dictionary))
    return random.sample(dictionary.items(), quantity)


def filter_tours(departure, tours):
    return dict(filter(lambda tour: tour[1]['departure'] == departure, tours.items()))


def find_min_max(items, item_key):
    return {
            'max': max(tour[item_key] for tour in items.values()),
            'min': min(tour[item_key] for tour in items.values()),
        }
