from random import choice


class Animal(object):
    def __init__(self, alive, big):
        self.__is_alive = alive
        self.is_big = big

    def voice(self):
        raise AttributeError


class Cat(Animal):
    def voice(self):
        print('Cat says: Meoooooooww...')


class Dog(Animal):
    def voice(self):
        print('Dog says: Bark, bark!')


class Tiger(Animal):
    def voice(self):
        print('Tiger says: RRRrrrrrrrr...')


class Wolf(Animal):
    def voice(self):
        print('Wolf says: OOOoooowwwwwwwww...')


class Fox(Animal):
    def voice(self):
        print('What does the fox say? Asd;asdlaksjdmla;ksmjdloafd')


class Owl(Animal):
    pass


def say_smth(obj):
    try:
        print(obj.__is_alive)
    except AttributeError:
        print('variable __is_alive is incapsulated!')
    print('Is {} big? {}'.format(type(exemplar).__name__, obj.is_big))
    obj.voice()


if __name__ == '__main__':
    animals = [Cat, Dog, Tiger, Wolf, Fox, Owl]
    vars = [True, False]
    for animal in animals:
        exemplar = animal(choice(vars), choice(vars))
        say_smth(exemplar)
