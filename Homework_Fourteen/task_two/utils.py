import random
import string


def random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))