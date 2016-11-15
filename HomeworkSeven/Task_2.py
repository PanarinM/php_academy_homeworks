answerlist = ['yes', 'no']

while True:
    while True:
        word_string = input('Input a string: ')
        if len(word_string) != 0:
            break
        else:
            continue

    words = {}
    word_string_split = word_string.split(' ')
    for word in word_string_split:
        words.setdefault(word, 0)
        words[word] += 1

    print(words)
    while True:
        answer = input('Again?')
        if answer in answerlist:
            break
        else:
            print('Yes or no!')
            continue
    if answer == 'yes':
        continue
    else:
        break