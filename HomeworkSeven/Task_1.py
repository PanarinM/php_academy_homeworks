unique = {}
user_input = input('Input the string: ')
user_input = user_input.split()
for word in user_input:
    clear_word = ''.join(i for i in word if i.isalnum())
    unique[clear_word] = ' '
print(unique)
