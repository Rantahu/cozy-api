from django.shortcuts import render

from rest_framework.filters import(
    SearchFilter,
    OrderingFilter
)

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response

from rest_framework.generics import(
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)

from rest_framework.views import APIView
from rest_framework import status


from .permissions import IsOwnerOrReadOnly


from rest_framework.authtoken.models import Token
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from .serializers import *

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


class ProfileList(ListAPIView):
    """
        This view is for API get request for a Profile

        Attributes:
            queryset: Query holding all of the Board Objects.
            serializer_class: Using the Profile List Serializer
            permission_classes: Anyone is allowed to view the list of Profiles,
            even unathenticated users
            search_field: Allow the query to be fiilted by the following attributes:
                name
            example: http://example.com/thread/user?search=Treyway
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    permission_classes = [AllowAny]
    search_fields = ('name')


class ProfileUpdate(RetrieveUpdateAPIView):
    """
        This view is for an API post request for Profile

        Attributes:
            queryset: Query holding all of the Profile objects
            serializer_class:Using Profile Create update serializer class
            permissions_classes = Only admin users are allowed to update profiles currently
            search_fields: Allow the query to be filtered by the following attributes:
                name
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'user__username'

    def perform_update(self, serializer):
        serializer.save()

class ProfileDetail(RetrieveAPIView):
    """
        This view for an APi get request for Profile

        Attributes:
            queryset: Query holding all of the Profile Objects
            serializer_class: Using profile detail serializer
            permission_classes: Any one is allowed to call a profile's detail
            even those who are unathenticated users
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'user__username'


class UserCreate(APIView):
    """
    Creates the user.
    """
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
