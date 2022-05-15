import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
def unique_rand():
    while True:
        id = User.objects.make_random_password(length=8)
        return id


class url(models.Model):
    id = models.CharField(max_length=8, unique=True, default=unique_rand,primary_key=True,editable=False)
    main_link = models.TextField()


