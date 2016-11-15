our_dict = {'one': 'two', 'three': 'four', 'five': 'six'}
keylist = []
valuelist = []
for i in our_dict.keys():
    keylist.append(i)
    valuelist.append(our_dict[i])
print(keylist)
print(valuelist)
