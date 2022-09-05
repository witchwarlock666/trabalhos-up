from django.db import models

class Game(models.Model):
    gameid = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    developers = models.CharField(max_length=200)
    publishers = models.CharField(max_length=200)
    price = models.CharField(max_length=12)
    release = models.CharField(max_length=20)
    background = models.CharField(max_length=1000, default="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3e9d67ac-08f4-4b70-b67a-2089c363385a/d9gsvdb-9281c06a-9de0-4b9b-9ec0-6d10aadae12e.png/v1/fill/w_1192,h_670,q_70,strp/steam_wallpaper_by_alyama123_d9gsvdb-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQ0MCIsInBhdGgiOiJcL2ZcLzNlOWQ2N2FjLTA4ZjQtNGI3MC1iNjdhLTIwODljMzYzMzg1YVwvZDlnc3ZkYi05MjgxYzA2YS05ZGUwLTRiOWItOWVjMC02ZDEwYWFkYWUxMmUucG5nIiwid2lkdGgiOiI8PTI1NjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.i1n53_K6L6n3X8vaqekaiZjxuE2yui5o5u_AECLtPbc")
    
    def __str__(self):
        return self.gameid
