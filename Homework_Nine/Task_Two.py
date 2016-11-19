# First solution
divider_seven = [i for i in range(1, 100000) if i % 7 == 0]
divider_three = [i for i in range(1, 100000) if i % 3 == 0]
answer = [i for i in divider_seven if i in divider_three]
print(answer)
# Second solution (As all of the elements of this list is unique by the task,
# we can use Sets and built-in function of intersect)
# this works much faster due to hashing nature of sets
# although much less readable as sets are unordered
divider_seven_2 = {i for i in range(1, 100000) if i % 7 == 0}
divider_three_2 = {i for i in range(1, 100000) if i % 3 == 0}
answer_2 = divider_seven_2.intersection(divider_three_2)
print(answer_2)