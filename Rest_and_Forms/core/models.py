from __future__ import unicode_literals

from django.db import models

from solo.models import SingletonModel

from utils import get_file_path


class Configuration(SingletonModel):
    header_img = models.FileField(upload_to=get_file_path, blank=True, null=True)
    about = models.TextField()
    terms_of_service = models.TextField()
    privacy_policy = models.TextField()

    def __str__(self):
        return "Our website configuration"
