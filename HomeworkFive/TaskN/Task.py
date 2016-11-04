# The task was to create stairs of eather numbers or stars
# I decided to also add pyramid shape feature as is requires more string sum shenanigans
# All parameters should be specified by the user and will be asked until he inputs a correct value
# Also pyramid and stairs scales with input to always stay the right shape (for example if 100 rows are specified:
#  all lower order numbers in pyramid and stairs will be 001, 002, etc. to keep the right shape)

# At start I declare all possible string inputs for user
answerlist = ['pyramid', 'stairs']
answerlist2 = ['yes', 'no']
answerlist3 = ['numbers', 'stars']

# All my program will repeat itself infinitely, until user specifies 'no' in the end
while True:
    # Here user must specify the resultant shape. I check if his input is in list of possible answers and if it is not,
    # i ask him again nicely, until he makes a correct input
    while True:
        y = input('Do you want to get pyramid or stairs? ')
        if y in answerlist:
            break
        else:
            print('Pyramid or stairs!')
            continue

    # Here user must specify what 'bricks' must be used, numbers or stairs.
    # I check if his input is in list of possible answers and if it is not,
    # i ask him again nicely, until he makes a correct input
    while True:
        j = input('Do you want to use numbers or stars? ')
        if j in answerlist3:
            break
        else:
            print('Numbers or stars!')
            continue

    # Here user must specify the number of rows.
    # I check if his input is integer value and if it is not,
    # i ask him again nicely, until he makes a correct input
    while True:
        try:
            x = int(input('Please input the number of rows: '))
            break
        except ValueError:
            print('Please enter an integer number!')
            continue

    # Part of code for stairs shape
    if y == 'stairs':
        for i in range(1, x+1):
            # Magical part of code that defines scalability and persistence of shape
            #  for numbers of order higher than one
            if j == 'numbers':
                n = len(str(x))
                l = n - len(str(i))
                p = '0' * l + str(i)
                print((str(p)+' ') * i)
            elif j == 'stars':
                print('* '*i)
        print('End of stairs!')

    # Part of code for pyramid shape
    elif y == 'pyramid':
        for i in range(1, x+1):
            # Magical part of code that defines scalability and persistence of shape
            #  for numbers of order higher than one
            if j == 'numbers':
                n = len(str(x))
                l = n - len(str(i))
                p = '0'*l + str(i)
                # Connecting strings in pyramid shape is much more interesting.
                # As I need to also maintain centration of rows with respect number order
                print((' '*(x-i))*n, (str(p)+' '*n)*i)
            elif j == 'stars':
                print(' ' * (x - i), '* ' * i)
        print('End of pyramid!')

    # Here user must specify if he wants to restart program.
    # I check if his input is 'yes' or 'no' and if it is not,
    # i ask him again nicely, until he makes a correct input
    while True:
        z = input('Again? ')
        if z in answerlist2:
            break
        else:
            print('Yes or no!')
            continue
    # If user answered 'yes' i continue to the next iteration of program
    if z == 'yes':
        continue
    # If 'no' program ends
    elif z == 'no':
        print('Bye!')
        break
    break
