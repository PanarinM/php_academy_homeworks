from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    COUNTRIES = (
        ("Ukraine", "Ukraine"),
        ("Russia", "Russia")
    )
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=255, choices=COUNTRIES, default="Ukraine")

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return "{} {} {} {}".format(self.username,
                                    self.first_name,
                                    self.last_name,
                                    self.country)

    def get_upper_email(self):
        return self.email.upper()
