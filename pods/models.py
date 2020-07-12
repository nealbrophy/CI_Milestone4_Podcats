from django.db import models


class Podcast(models.Model):

    uuid = models.UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=200)
    language = models.CharField(max_length=100)
    categories = models.TextField()
    website = models.URLField(max_length=200)
    author = models.CharField(max_length=200)
    itunes_id = models.IntegerField()

    def __str__(self):
        return self.title
