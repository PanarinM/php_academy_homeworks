# this is the program for printing the table of multiplication

# i use the cycle in cycle for easier and more clear output
# By connecting string i receive a more understandable form
for i in range(1, 11):
    for j in range(1, 11):
        print(str(i)+'x'+str(j)+'='+str(i*j))
    print()
