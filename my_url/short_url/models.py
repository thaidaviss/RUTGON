from django.db import models
from django.db.models import Model

# Create your models here.
class MyUrl(Model):
    alias = models.CharField(max_length=200)
    url = models.CharField(max_length=5000)
