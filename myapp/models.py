from django.db import models

class xyz(models.Model):
    title=models.CharField(max_length=100)
    publishDate=models.CharField(max_length=100)
    paperPath=models.CharField(max_length=100)


class xyz1(models.Model):
    path=models.CharField(max_length=100)
    link=models.CharField(max_length=100)
   