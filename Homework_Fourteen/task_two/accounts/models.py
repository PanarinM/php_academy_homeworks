from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_upper_email(self):
        return self.email.upper()
