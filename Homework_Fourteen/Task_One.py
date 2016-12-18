class Iterator(object):
    def __init__(self, filename):
        self.filename = open(filename, 'r', encoding='UTF-8')

    def __iter__(self):
        return self

    def next(self):
        for lines in self.filename:
            return lines.strip()
        raise StopIteration

    def close(self):
        self.filename.close()

    def __del__(self):
        self.filename.close()


if __name__ == '__main__':
    a = Iterator('./trash/test')
    try:
        print(a.next())
        print(a.next())
        print(a.next())
        print(a.next())
        print(a.next())
        print(a.next())
        print(a.next())
    except StopIteration:
        print('no more lines!')

