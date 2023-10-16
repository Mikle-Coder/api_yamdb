from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.slug


class Genre(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.slug


class Title(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.IntegerField(
        default=None,
        null=True
    )
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="titles", null=True)
    genre = models.ManyToManyField(Genre, related_name="titles")

    def __str__(self) -> str:
        return self.name