from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Title, Category, Genre
from reviews.models import Review
from django.db.models import Avg


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    rating = SerializerMethodField()

    class Meta:
        model = Title
        fields = '__all__'

    def get_rating(self, obj):
        reviews = Review.objects.filter(title=obj)
        if reviews.exists():
            average_rating = reviews.aggregate(Avg('score'))['score__avg']
            return average_rating
        return None