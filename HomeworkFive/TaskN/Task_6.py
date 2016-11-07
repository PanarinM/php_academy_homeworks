# In this program i calculate the sum of digits in a string
# string can be any type as in my program i delete from string everything except digits

# firstly i initialize a variable for sum
result = 0

# i ask the user for input. There is no cycle for this input as any input is valid
y = input('Input a string: ')

# i recreate a string with digits only by iterating through an original string and adding to the new one values
# that are digits
userstring = ''.join(i for i in y if i.isdigit())

# If the result string is empty, then user input had no digits in it
if len(userstring) == 0:
    print('There is no digits in this string!')
else:
    # else, i iterate through the resultant string and add each value to the result
    for i in userstring:
        result += int(i)
    # printing out the result
    print('Digits in this string: '+str(userstring))
    print('The sum of digits in this string is equal to: '+str(result))
