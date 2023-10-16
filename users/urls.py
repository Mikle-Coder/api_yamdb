from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, auth_email, auth_token, users_me


router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('auth/email/', auth_email, name='auth_email'),
    path('auth/token/', auth_token, name='api_group'),
    path('users/me/', users_me, name='users_me'),
]

urlpatterns += router.urls