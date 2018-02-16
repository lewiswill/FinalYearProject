from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class user_headline_model(models.Model):
    user_headline = models.CharField(max_length=200)
    created = models.DateTimeField(default=datetime.now, blank=True)