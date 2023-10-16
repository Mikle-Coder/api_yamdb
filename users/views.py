from rest_framework.response import Response
from rest_framework import status, filters
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny
from api_yamdb.permissions import IsSuperuser
from .serializers import UserSerializer

from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


@api_view(['POST']) 
@permission_classes([AllowAny])
def auth_email(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        confirmation_code = get_random_string(length=6)
        serializer.save(confirmation_code=confirmation_code)
        
        message = f'Your confirmation code: {confirmation_code}'
        send_mail('Confirmation Code', message, 'admin@yamdb.fake', [email])
        return Response({"Check your email for confirmation code": email}, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST']) 
@permission_classes([AllowAny])
def auth_token(request):
    email = request.data.get('email')
    confirmation_code = request.data.get('confirmation_code')

    user = User.objects.filter(email=email).first()
    if not user:
        return Response({'detail': 'User with this email does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    if user.confirmation_code == confirmation_code:
        token = str(RefreshToken.for_user(user).access_token)
        return Response({'token': token}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Invalid confirmation code.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH']) 
def users_me(request):
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperuser]
    filter_backends = [filters.SearchFilter]
    lookup_field = 'username'