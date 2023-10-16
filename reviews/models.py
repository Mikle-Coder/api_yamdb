from django.db import models
from titles.models import Title
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator



User = get_user_model()


class Review(models.Model):
    text = models.TextField()
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    score = models.IntegerField(
        default=0, 
        validators=[
            MaxValueValidator(limit_value=10),
            MinValueValidator(limit_value=1),
        ]
    )
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    
    class Meta():
        unique_together = ('author', 'title',)


    def __str__(self) -> str:
        return self.text


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата добавления", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")

    def __str__(self) -> str:
        return self.text