import random
import string
import uuid
import os


def random_word(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.__class__.__name__.lower(), filename)

