# 1. Создаем список запрещенных слов из ввода пользователя
# 2. записываем в переменную строку из ввода пользователя
# 3. разбиваем строку по пробелам
# 4. с помощью цикла for проходим по словам строки
#   4.1 если слово есть в списке запрещеных, то заменяем его на ***

# Метод 1

# taboo = input('Input taboo words')
# taboo = taboo.split(' ')
#
# user_input = input('Input the string to be checked')
# user_input = user_input.split(' ')
#
# for word in range(0, len(user_input)):
#     if user_input[word] in taboo:
#         user_input[word] = '***'
#     else:
#         continue
#
# print(' '.join(user_input))

# Метод 2

taboo = input('Input taboo words: ')
taboo = taboo.split(' ')

user_input = input('Input the string to be checked: ')

for word in taboo:
    user_input = user_input.replace(word, '***')

print(user_input)