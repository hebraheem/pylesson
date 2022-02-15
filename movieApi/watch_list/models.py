from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about=models.TextField(max_length=250)
    website= models.URLField(max_length=150)

    def __str__(self):
        return  self.name


class WatchList(models.Model) :
    title = models.CharField(max_length=50)
    description= models.TextField(max_length=500)
    published = models.BooleanField(default=False)
    streamingPlatform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(max_length=500, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    verified = models.BooleanField(default=False)
    movie = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="review")

    def __str__(self):
        return str(self.rating) + " | " + self.movie.title