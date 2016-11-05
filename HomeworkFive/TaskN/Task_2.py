# Парные / непарные
answerlist = ['even', 'odd']
while True:
    y = input('Do you want to get even or odd numbers? ')
    if y in answerlist:
        break
    else:
        print('Even or odd!')
        continue

while True:
    try:
        x = int(input('Input the limit number: '))
        break
    except ValueError:
        print('Input an integer!')
        continue

for i in range(0, x + 1):
    if i % 2 == 0:
        if y == 'even':
            print(i)
    else:
        if y == 'odd':
            print(i)