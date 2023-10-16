from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from api_yamdb.permissions import IsSuperuser, IsOwner

from titles.models import Title
from .models import Review
from .serializers import ReviewSerializer, CommentSerializer



class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        try:
            serializer.save(author=self.request.user, title=title)
        except IntegrityError:
            raise ValidationError("Автор уже оставил свой обзор на это проивзедение.")


    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()


    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        else: 
            permission_classes = [IsOwner|IsAdminUser|IsSuperuser]
        return [permission() for permission in permission_classes]
    

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)


    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all()


    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        else: 
            permission_classes = [IsOwner|IsAdminUser|IsSuperuser]
        return [permission() for permission in permission_classes]