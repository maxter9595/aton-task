from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if self.first_name and self.last_name:
            self.full_name = f'{self.first_name} {self.last_name}'
        super(User, self).save(*args, **kwargs)
