while True:
    try:
        x = int(input('Please input the length of the list: '))
        break
    except ValueError:
        print('Please enter an integer number!')
        continue

thelist = []
for i in range(0, x):
    y = input('Input the ' + str(i) + 'th value: ')
    thelist.append(y)

print('Entered list: '+', '.join(thelist))

dellist = []
for i in range(0, len(thelist)):
    if len(thelist[i]) > 5:
        dellist.append(i)

for i in range(0, len(dellist)):
    del thelist[dellist[-1-i]]

print('The list after deletion of elements bigger than 5: '+', '.join(thelist))
