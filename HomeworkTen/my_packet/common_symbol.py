# 1. Написати скріпт, який приймає параметром ім’я файлу і повертає найчастіше вживаний символ в файлі.
# Case insensitive. Якщо найпопулярніший пробіл - взяти наступний за ним.
# 2. Якщо користувач не передав файл параметром, попросити в нього ввести ім’я файлу вручну.
# Якщо такого файлу немає, повторно попросити про ввід
from collections import Counter
from sys import argv


def get_most_common_symbol(c=None):
    """Starting point for this module. Checks system arguments for a file and executes a function to find
    the most common symbol. If there is none, asks user to input a file

    returns tuple of dictionaries. Key = symbol, value = amount"""
    if c is None:
        try:
            c = argv[1]
        except IndexError:
            while True:
                answ = input('Parameter was not set, do you want to input it yourself? [y / n] ')
                if answ == 'y':
                    c = input('Input filename ')
                    break
                elif answ == 'n':
                    print('exiting...')
                    exit()
                else:
                    print('y for yes, n for no please!')
    return open_file(c)


def open_file(file_name):
    """Opens the file for further work

    returns tuple of dictionaries. Key = symbol, value = amount"""
    while True:
        try:
            with open(file_name, 'r', encoding='UTF-8') as a:
                text = a.read().lower().replace(" ", "")
                result1 = working_pony(text)
                result2 = working_pony_2(text)
                return result1, result2
        except FileNotFoundError:
            while True:
                text = 'File ' + file_name + ' was not found, do you want to reinput it yourself? [y / n] '
                answ = input(text)
                if answ == 'y':
                    file_name = input('Input filename ')
                    break
                elif answ == 'n':
                    print('exiting...')
                    exit()
                else:
                    print('y for yes, n for no please!')


def working_pony(texttocheck):
    """First solution. Iterates through given string and adds symbols to dictionary, also counting their appearance

    Takes string as an input

    returns dictionary of the most common symbol with key = symbol, value = amount

    Note: if their is more than one most common symbols, it will output them all"""
    result = {}
    for symbol in texttocheck:
        result[symbol] = result.get(symbol, 0) + 1
    return{k: v for k, v in result.items() if v == max(result.values())}


def working_pony_2(texttocheck):
    """Second solution. Using the Counter module from collections we can calculate
    most common symbol with most_common function

    Takes string as an input

    returns dictionary of the most common symbol with key = symbol, value = amount

    Note: if their is more than one most common symbols, it will output only one"""
    return dict(Counter(texttocheck).most_common(1))


if __name__ == '__main__':
    print(get_most_common_symbol())
