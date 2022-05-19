from django.db import models

from django.conf import settings


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

    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
