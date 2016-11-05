result = 0
y = input('Input a string: ')
userstring = ''.join(i for i in y if i.isdigit())
if len(userstring) == 0:
    print('There is no digits in this string!')
else:
    for i in userstring:
        result += int(i)
    print('Digits in this string: '+str(userstring))
    print('The sum of digits in this string is equal to: '+str(result))
