from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews')
router.register(r'titles/\d+/reviews/(?P<review_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = router.urls