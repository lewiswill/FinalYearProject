from django.db import models

# Create your models here.
class real_news_headlines_dataset(models.Model):
    headline = models.CharField(max_length=200)
    headline_status = models.CharField(max_length =5)

class fake_news_headlines_dataset(models.Model):
    headline = models.CharField(max_length=200)
    headline_status = models.CharField(max_length =5)
