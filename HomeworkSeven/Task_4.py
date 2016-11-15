# 1. Записываем пользовательскую строку в переменную
# 2. записываем вторую пользовательскую строку во вторую переменную
# 3. разделяем первую строку по пробелам
# 4. с помощью .find смотрим есть ли такое слово во второй строке
# 5. Если есть, то добавляем его в список
# 6. выводим список

user_input_one = input('Input first string: ')
user_input_two = input('Input second string: ')
intersectionlist = []
user_input_two = ' '+user_input_two+' '
user_input_one = user_input_one.split(' ')
for word in user_input_one:
    new_word = ''.join(i for i in word if i.isalnum())
    new_word = ' '+new_word+' '
    if user_input_two.find(new_word) >= 0:
        intersectionlist.append(new_word.strip())
print(intersectionlist)