from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    lyrics = models.TextField()

    def __str__(self):
        return self.title
