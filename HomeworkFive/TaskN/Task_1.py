# This program calculates maximum and minimum of provided list
# The user must input the length of a list and list elements

# Here i ask user to input the length of the list as an integer value
# If the user inputs non-integer value, i'll ask him to make a correct
# input until he does so
while True:
    try:
        x = int(input('Input the length of a list as integer: '))
        break
    except ValueError:
        print('Input an integer!')
        continue

# Here i initialize an empty list to put the user inputted values
tasklist = []

# I run a for cycle fromm zero to user inputted value, so the user can
# fill the list with values
for i in range(0, x):
    # I'll repeat asking him for input until the user makes a proper one
    while True:
        try:
            f = float(input('Input the '+str(i)+'th value: '))
            break
        except ValueError:
            print('Entered value is not a number!')
            continue
    tasklist.append(f)

# Here i calculate max and min with use of list functions
print('The max value of this list is: '+str(max(tasklist)).strip())
print('The min value of this list is: '+str(min(tasklist)).strip())
