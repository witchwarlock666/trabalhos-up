from django.db import models

class Game(models.Model):
    gameid = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    developers = models.CharField(max_length=200)
    publishers = models.CharField(max_length=200)
    price = models.CharField(max_length=12)
    release = models.CharField(max_length=20)
    
    def __str__(self):
        return self.gameid
