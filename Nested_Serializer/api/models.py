from turtle import title
from unicodedata import name
from django.db import models

class Singer(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Song(models.Model):
    title=models.CharField(max_length=50)
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='sungby')
    duration=models.IntegerField()

    def __str__(self):
        return self.title
