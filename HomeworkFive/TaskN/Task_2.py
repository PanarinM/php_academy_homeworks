# This program prints odd or even values from 0 till the user input

# Here i initialize a list of possible answers for user
answerlist = ['even', 'odd']

# This cycle prevents user from entering non-valid value
# i will ask user for a valid one until he does so
while True:
    y = input('Do you want to get even or odd numbers? ')
    if y in answerlist:
        break
    else:
        print('Even or odd!')
        continue

# This cycle prevents user from entering non-valid value
# i will ask user for a valid one until he does so
while True:
    try:
        x = int(input('Input the limit number: '))
        break
    except ValueError:
        print('Input an integer!')
        continue

# Here is the part of code, where i check the value to be even by modulo division
for i in range(0, x + 1):
    if i % 2 == 0:
        if y == 'even':
            print(i)
    else:
        if y == 'odd':
            print(i)