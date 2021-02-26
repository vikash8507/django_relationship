from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cat = models.CharField(max_length=100)
    pul_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cat = models.CharField(max_length=100)
    pul_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    cat = models.CharField(max_length=100)
    pul_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
