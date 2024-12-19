from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField(max_length=100)

class AccessRecords(models.Model):
    topic_name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    autor=models.CharField(max_length=100)
    date=models.DateField(max_length=100)
