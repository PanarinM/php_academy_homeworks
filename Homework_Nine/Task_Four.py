python_studs = {2: 'Ivan', 17: 'Artem', 18: 'Sergiy', 21: 'Antuan', 34: 'Anton', 35: 'Stepan', 37: 'Sergiy',
                43: 'Artem', 44: 'Antuan',  51: 'Sergiy', 60: 'Antuan', 61: 'Sergiy', 62: 'Stepan', 78: 'Artem',
                79: 'Stepan', 82: 'Ivan', 90: 'Antuan', 94: 'Antuan', 95: 'Ivan'}

js_studs = {0: 'Antuan', 7: 'Sergiy', 10: 'Anton', 16: 'Ivan', 17: 'Ivan', 23: 'Ivan', 33: 'Ivan', 34: 'Antuan',
            39: 'Ivan', 45: 'Artem', 47: 'Stepan', 58: 'Stepan', 66: 'Stepan', 67: 'Sergiy', 71: 'Sergiy', 73: 'Antuan',
            87: 'Stepan', 94: 'Antuan', 96: 'Stepan'}


def both_leng(dict1, dict2):
    """Intersect two dictionaries using list comprehensions
        Takes 2 dictionaries as parameters"""
    return {i: dict1[i] for i in (dict1.keys() & dict2.keys())}


def at_least_one(dict1, dict2):
    """Union of two dictionaries with update function
        Takes 2 dictionaries as parameters"""
    dict1.update(dict2)
    return dict1


def only_one(dict1, dict2):
    """Symmetric difference of two dictionaries
        Takes 2 dictionaries as parameters"""
    inter = both_leng(dict1, dict2)
    dict1 = at_least_one(dict1, dict2)
    dict1 = {k: v for k, v in dict1.items() if k not in inter}
    return dict1

print('Learning both languages:', both_leng(python_studs.copy(), js_studs.copy()))
print('Learning at least one language:', at_least_one(python_studs.copy(), js_studs.copy()))
print('Learning only one language:', only_one(python_studs.copy(), js_studs.copy()))
