while True:
    try:
        x = int(input('Input the length of a list as integer: '))
        break
    except ValueError:
        print('Input an integer!')
        continue

tasklist = []
for i in range(0, x):
    while True:
        try:
            f = float(input('Input the '+str(i)+'th value: '))
            break
        except ValueError:
            print('Entered value is not a number!')
            continue
tasklist.append(f)

print('The max value of this list is: '+str(max(tasklist)).strip())
print('The min value of this list is: '+str(min(tasklist)).strip())
