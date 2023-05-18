from django.contrib.auth.models import AbstractUser
from django.db import models


class User (AbstractUser):
    """User models"""

    about = models.CharField('About_you', max_length=100, blank=True)
    avatar = models.ImageField('Avatar',  upload_to='users/', blank=True)
    email = models.EmailField('E-mail', unique=True, blank=False)
    birthday = models.DateField('Birthday', blank=True, null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
