from django.db import models


class Menu(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )
    image_url = models.URLField()
    ingredients = models.TextField()
    cooking_time = models.IntegerField(default=0)
    description = models.TextField()
