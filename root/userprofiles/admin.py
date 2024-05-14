from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(user_profile)
admin.site.register(disease)
admin.site.register(person_to_disease)