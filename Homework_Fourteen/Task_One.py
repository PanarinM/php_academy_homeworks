class Myiterator(object):
    def __init__(self, filename):
        self.filename = open(filename, 'r', encoding='UTF-8')

    def __iter__(self):
        return self

    def __next__(self):
        for lines in self.filename:
            return lines
        raise StopIteration

    def __del__(self):
        self.filename.close()


def Mygenerator(filename):
    with open(filename, 'r', encoding='UTF-8') as a:
        for lines in a:
            yield lines


def iterate_through(iter):
    try:
        while True:
            print(next(iter).strip())
    except StopIteration:
        print('no more lines!')

if __name__ == '__main__':
    a = Myiterator('./trash/test')
    iterate_through(a)

    b = Mygenerator('./trash/test')
    iterate_through(b)