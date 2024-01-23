from django.db import models


# Create your models here.
class DataInsert(models.Model):
    name = models.CharField(max_length=200, default="x")
    title = models.CharField(max_length=200, default="x")


class Post(models.Model):
    author = models.CharField(max_length=200, default="x")
