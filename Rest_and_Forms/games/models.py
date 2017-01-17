from __future__ import unicode_literals

from django.db import models

from accounts.models import User

from utils import get_file_path


class Game(models.Model):
    ACTIVITY_CHOICES = (
        ("Football", "Football"),
        ("Hockey", "Hockey"),
    )
    image = models.FileField(upload_to=get_file_path, blank=True, null=True)
    members = models.ManyToManyField(User, related_name="members")
    top_user = models.OneToOneField(User, related_name="top_user", blank=True, null=True)
    activity = models.CharField(max_length=255, choices=ACTIVITY_CHOICES, default="Football")
    creator = models.ForeignKey(User, related_name="creator")
    views = models.PositiveIntegerField(default=0)
    date_end = models.DateField()

    def __str__(self):
        return self.activity

