from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=225)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)