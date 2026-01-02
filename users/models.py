from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy


class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email



class UserProfile(models.Model):
    user        = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='profile')
    first_name  = models.CharField(max_length=100, blank=True, null=True)
    last_name   = models.CharField(max_length=100, blank=True, null=True)
    image_url   = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    long_bio    = models.TextField(max_length=500, blank=True, null=True)
    short_bio   = models.CharField(max_length=150, blank=True, null=True)
    facebook    = models.URLField(max_length=200, blank=True, null=True)
    twitter     = models.URLField(max_length=200, blank=True, null=True)
    linkedin    = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse_lazy('edit_profile', kwargs={'pk': self.pk})
