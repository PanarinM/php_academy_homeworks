# This program asks for user input of length of the list as well as the list elements themselves

# This cycle prevents user from entering non-valid value
# i will ask user for a valid one until he does so
while True:
    try:
        x = int(input('Please input the length of the list: '))
        break
    except ValueError:
        print('Please enter an integer number!')
        continue

# here i initialize an empty list for user inputs
thelist = []
for i in range(0, x):
    y = input('Input the ' + str(i) + 'th value: ')
    thelist.append(y)

# outputting the list for user to see, before transformation
print('Entered list: '+', '.join(thelist))

# Iterating the list backwards to prevent deletion of elements to disrupt indexes
for i in range(-len(thelist), 0):
    if len(thelist[i]) > 5:
        del thelist[i]

# output of the list after transformation
print('The list after deletion of elements bigger than 5: '+', '.join(thelist))
