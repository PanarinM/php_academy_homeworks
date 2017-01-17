from django.core.management.base import BaseCommand

from accounts.models import User

from utils import random_word


class Command(BaseCommand):
    help = 'Create dummy users'

    def handle(self, *args, **options):
        for item in xrange(100):
            User.objects.create(first_name=random_word(6),
                                last_name=random_word(6),
                                username=random_word(6),
                                email="{}@gmail.com".format(random_word(6)),
                                password=random_word(6))
