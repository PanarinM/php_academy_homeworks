# Напишіть декоратор, який вказує на типи даних, що повинні бути передані в функцію.
# Якщо введені дані не відповідного типу - рейзимо Exception.
# Декоруємо функцію, що просто виводить введені аргументи на екран.


def typechecker(*args):
    """
    decorator that checks if the passed arguments into functions have the correct type
    is indifferent to the amount of args function has
    :param args:
    :return:
    """
    types_lst = [i for i in args]
    
    def typeschecker(func):
        def deco(*args):
            compare = zip(types_lst, args)
            for i in list(compare):
                if not isinstance(i[1], i[0]):
                    raise TypeError
            func(*args)
        return deco
    return typeschecker


@typechecker(str, str, int)
def func(one, two, three):
    print(one+two, three)


@typechecker(str, str, int, int)
def func2(one, two, three, four):
    print(one + two, three+four)

if __name__ == '__main__':
    try:
        func('1', '2', '3')
    except TypeError:
        print('Type error was raised for func')

    func('1', '2', 3)

    try:
        func2('1', '2', '3', '4')
    except TypeError:
        print('Type error was raised for func2')

    func2('1', '2', 3, 4)
