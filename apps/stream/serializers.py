from rest_framework.serializers import(
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    RelatedField,
    ReadOnlyField,
    PrimaryKeyRelatedField,
    ReadOnlyField,
    Field
    )

from rest_framework.validators import UniqueValidator
from rest_framework import serializers
# from django.contrib.auth.models import User

from apps.accounts.serializers import ProfileDetailSerializer
from .models import Stream

class StreamCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Stream
        fields = [
            'title',
            'description',
            'channel',
            'live'
        ]

class StreamDetailSerializer(ModelSerializer):
    streamer = ProfileDetailSerializer(read_only = True)
    class Meta:
        model = Stream
        fields = [
            'id',
            'title',
            'description',
            'channel',
            'live',
            'viewers',
            'featured',
            'streamer'
        ]

class StreamListSerializer(ModelSerializer):
    streamer = ProfileDetailSerializer(read_only = True)
    class Meta:
        model = Stream
        fields = [
            'id',
            'title',
            'live',
            'viewers',
            'streamer'
        ]
