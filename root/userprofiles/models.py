from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_profile(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pfp = models.ImageField(default='')
    bio = models.TextField(max_length=300)

    def __str__(self):
        return self.user.username