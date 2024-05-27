from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_profile(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300)

    def __str__(self):
        return self.user.username


class disease(models.Model) :
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class person_to_disease(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease = models.ForeignKey("userprofiles.disease", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} --> {self.disease.name}"
