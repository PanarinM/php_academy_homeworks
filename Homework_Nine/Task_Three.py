import random
# Solution One
# I generate a list of random values using list comprehension and
# uniformal pseudo-random numbers from 'random' module int(random.uniform(0, 400))
random_list = [random.randint(0, 400) for i in range(0, 100)]
# Using the built-in sort function with reversed key argument i receive a sorted list, ordered by decline
random_list.sort(reverse=True)
# Taking simply the 2nd element is not enough as in list there can be repeated elements
# i will check elements of list if they are equal to the first one and will take the first that is not as a result
i = 0
while True:
    if random_list[0] == random_list[i]:
        i += 1
    else:
        result = random_list[i]
        break

print(random_list)
print(result)

# Solution Two
# We can overcome the problem of repeatable numbers by using a set instead
# On the other hand we won't receive the required length of set reliably as if randomiser will generate a repetition
# set rules will just omit the step
random_list_2 = {random.randint(0, 400) for i in range(0, 100)}
# Sorted built-in function returns sorted list out of any iteratable element
# Reversed function reverses the list
random_list_2 = list(sorted(random_list_2))
# as elements of the set ar unique, second element of the resultant list will always be second largest
result_2 = random_list_2[-2]
print(random_list_2)
print(result_2)

# Solution Three
# There is a way to create a random unique list of desired length by generating one with range
# first and then shuffling it with random.shuffle function
random_list_3 = [i for i in range(0, 100)]
random.shuffle(random_list_3)
# after sorting it back and reversing we can take second element as the second largest
random_list_3.sort(reverse=True)
print(random_list_3)
result_3 = random_list_3[1]
print(result_3)

# Solution Four
# Another way is to use sets and add random elements until our set is required length.
# After that repeat steps from solution two
random_list_4 = set()
while len(random_list_4) != 100:
    random_list_4.add(random.randint(0, 400))
random_list_4 = list(sorted(random_list_4))
print(random_list_4)
result_4 = random_list_4[-2]
print(result_4)