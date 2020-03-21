from django.shortcuts import render

from rest_framework.filters import(
    SearchFilter,
    OrderingFilter
)

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response

from rest_framework.views import APIView


from rest_framework.generics import(
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework.views import APIView
from rest_framework import status


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from .permissions import IsStreamerOrReadOnly, IsUserOrReadOnly, IsUploaderOrReadOnly
from .serializers import *

from django.contrib.auth.models import User


# Create your views here.

class StreamList(ListAPIView):
    queryset = Stream.objects.all()
    serializer_class = StreamListSerializer
    permission_classes = [AllowAny]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['user__username', 'title', 'description', 'featured']
    ordering_fields = ['viewers', 'live']


class StreamDetail(RetrieveAPIView):
    queryset = Stream.objects.all()
    serializer_class = StreamDetailSerializer
    permission_classes = [AllowAny]

class StreamUpdate(RetrieveUpdateAPIView):
    queryset = Stream.objects.all()
    serializer_class = StreamCreateUpdateSerializer
    permission_classes = [IsStreamerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()
