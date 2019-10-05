from rest_framework.serializers import (
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

from .models import Board, Post, Thread
from apps.accounts.models import Profile
from apps.accounts.serializers import ProfileDetailSerializer



class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'message',
            'poster',
            'thread',
            'image',
            'board',
        ]


class PostDetailSerializer(ModelSerializer):
    poster = ProfileDetailSerializer(read_only = True)
    class Meta:
        model = Post
        image = SerializerMethodField()

        fields = [
            'id',
            'bid',
            'created',
            'poster',
            'message',
            'image'
        ]

        def get_image(self,obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image

class PostListSerializer(ModelSerializer):
    poster = ProfileDetailSerializer(read_only = True)
    class Meta:
        model = Post
        image = SerializerMethodField()
        fields = [
            'id',
            'bid',
            'created',
            'poster',
            'message',
            'image'
        ]

class ThreadCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'message',
            'poster',
            'image',
            'board'
        ]

class ThreadUpdateSerializer(ModelSerializer):
    class Meta:
        model = Thread
        fields = [
            'title',
            'blurb',
            'poster',
            'image',
            'board',
            'status'
        ]

class ThreadDetailSerializer(ModelSerializer):
    posts = PostDetailSerializer(many = True, read_only = True)
    poster = ProfileDetailSerializer(read_only = True)
    class Meta:
        image = SerializerMethodField()
        model = Thread
        fields = [
            'id',
            'title',
            'bid',
            'created',
            'poster',
            'tag',
            'blurb',
            'board',
            'replyCount',
            'latestReplyTime',
            'views',
            'imageCount',
            'posts',
            'image',
            'status'

        ]

        def get_image(self,obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image

class ThreadListSerializer(ModelSerializer):
    blurb = ReadOnlyField()
    poster = ProfileDetailSerializer(read_only = True)

    class Meta:
        image = SerializerMethodField()
        model = Thread
        fields = [
            'id',
            'bid',
            'title',
            'blurb',
            'views',
            'replyCount',
            'imageCount',
            'created',
            'poster',
            'board',
            'image'

        ]

        def get_image(self,obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image


class BoardListSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = [
            'name',
            'tag'
        ]

class BoardDetailSerializer(ModelSerializer):
    threads = ThreadListSerializer(many=True, read_only=True)
    activeThreads = ThreadListSerializer(many=True, read_only=True)
    latestPost = ThreadDetailSerializer(read_only = True)
    lookup_field = 'tag'
    class Meta:
        model = Board
        fields = [
            'name',
            'tag',
            'threads',
            'latestPost',
            'activeThreads'
        ]
class BoardActiveThreadsSerializer(ModelSerializer):
    activeThreads = ThreadListSerializer(many=True, read_only=True)
    latestPost = ThreadDetailSerializer(read_only = True)
    lookup_field = 'tag'
    class Meta:
        model = Board
        fields = [
            'id',
            'name',
            'tag',
            'latestPost',
            'activeThreads'
        ]

class BoardLockedThreadsSerializer(ModelSerializer):
    lockedThreads = ThreadListSerializer(many=True, read_only=True)
    latestPost = ThreadDetailSerializer(read_only = True)
    lookup_field = 'tag'
    class Meta:
        model = Board
        fields = [
            'id',
            'name',
            'tag',
            'latestPost',
            'lockedThreads'
        ]
        
class BoardArchivedThreadsSerializer(ModelSerializer):
    archivedThreads = ThreadListSerializer(many=True, read_only=True)
    latestPost = ThreadDetailSerializer(read_only = True)
    lookup_field = 'tag'
    class Meta:
        model = Board
        fields = [
            'id',
            'name',
            'tag',
            'latestPost',
            'archivedThreads'
        ]

class BoardCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = [
            'name',
            'tag'
        ]
