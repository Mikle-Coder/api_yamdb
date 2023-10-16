from rest_framework.viewsets import ModelViewSet
from .models import Title, Category, Genre
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer
from api_yamdb.permissions import IsSuperuser, IsReadOnly

from rest_framework import filters
from .filters import TitleFilter

from rest_framework.exceptions import ValidationError
from django.http import QueryDict


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperuser|IsReadOnly]
    filter_backends = [filters.SearchFilter]
    lookup_field = 'slug'
    http_method_names = ['get', 'post', 'delete']
    search_fields = ['name']


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsSuperuser|IsReadOnly]
    filter_backends = [filters.SearchFilter]
    lookup_field = 'slug'
    http_method_names = ['get', 'post', 'delete']
    search_fields = ['name']


class TitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsSuperuser|IsReadOnly]
    filterset_class = TitleFilter
    http_method_names = ['get', 'post', 'delete', 'patch']


    def get_category_obj(self, data):
        if slug := data.get('category'):
            try:
                return Category.objects.get(slug=slug)
            except Category.DoesNotExist:
                raise ValidationError({"Error" : "Category not found"})
    
    
    def get_genre_obj(self, data):
        slugs = data.getlist('genre') if isinstance(data, QueryDict) else data.get('genre')
        if slugs:
            try:
                print(slugs)
                return Genre.objects.filter(slug__in=slugs)
            except Genre.DoesNotExist:
                raise ValidationError({"Error" : "Genre not found"})


    def perform_create(self, serializer):
        data = self.request.data

        if category:= self.get_category_obj(data):
            serializer.save(category=category)

        if genre:= self.get_genre_obj(data):
            serializer.save(genre=genre)


    def perform_update(self, serializer):
        self.perform_create(serializer)
