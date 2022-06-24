from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1 ,'ADMIN'),
        (2 ,'TEACHER'),
        (3 ,'STUDENT'),
    )

    user_type = models.CharField (choices=USER,max_length=50, default=1)
    profile_pics = models.ImageField(upload_to = 'media/profile_pic')