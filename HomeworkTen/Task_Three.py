# Написати скріпт, який шукатиме передане як параметр або введене через input(аналогіно до першої задачі)
# ім’я файлу в директорії та усіх її піддиректоріях. Результатом має бути повний та відносний(від місця пошуку)
# шлях до файлу.
import os
from sys import argv


def find_file(file_name=None, directory='..'):
    if file_name is None:
        try:
            file_name = argv[1]
            return working_pony(file_name, directory)
        except IndexError:
            while True:
                anw = input('The argument is not passed, do you want to input one yourself? [y / n] ')
                if anw == 'y':
                    splittedline = input('file name(you can add directory after coma): ').split(',')
                    if len(splittedline) < 2:
                        splittedline.append(directory)
                    file_name = splittedline[0].strip()
                    directory = splittedline[1].strip()
                    return working_pony(file_name, directory)
                elif anw == 'n':
                    print('Exiting...')
                    exit()
                else:
                    print('unsupported answer!')
    else:
        return working_pony(file_name, directory)


def working_pony(file_name, direc='..'):
    result = []
    for a in os.walk(direc):
        if file_name in a[2]:
            result.append((a[0] + '\\' + file_name, os.path.abspath(a[0] + '\\' + file_name)))
    if len(result) == 0:
        raise FileNotFoundError
    else:
        return result


if __name__ == '__main__':
    print(find_file())
