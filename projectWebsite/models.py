from django.db import models

# Create your models here.
class UserNewsHeadline(models.Model):
    user_headline = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
