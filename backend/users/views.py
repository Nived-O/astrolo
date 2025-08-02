from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    """
    GET: List all users
    POST: Create a new user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User registered successfully!',
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Registration failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a user by ID
    PUT: Update a user
    DELETE: Delete a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def user_by_email(request, email):
    """
    GET: Retrieve a user by email
    """
    try:
        user = User.objects.get(email=email)
        serializer = UserSerializer(user)
        return Response({
            'message': 'User found',
            'user': serializer.data
        }, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({
            'message': 'User not found'
        }, status=status.HTTP_404_NOT_FOUND)
