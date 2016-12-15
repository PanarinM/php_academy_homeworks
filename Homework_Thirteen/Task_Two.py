def voice(self):
    # if self.__name__ == 'Owl':
    #     raise AttributeError
    # else:
    #     print('Voices!!!')
    print(self.is_big)


# class NewMetaTooOP(type):
#     def __new__(cls, name, parent, attr):
#         return super(NewMetaTooOP, cls).__new__(cls, name, parent, {'voice': voice})


class Animal:
    __is_alive = True
    is_big = True


# a = NewMetaTooOP('Tiger', (Animal,), {})
# a = Animal()
a = type('Tiger', (Animal,), {'voice': voice})
print(a.is_big)
a.voice()
print(a.__class__)
print(a.__bases__)
print(a.__name__)
