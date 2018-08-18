from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from datetime import datetime
from apps.accounts.models import Profile
# Create your models here.

class Board(models.Model):
    """This is a class for the Board Object

    Attributes:
        name: A string that holds the name of the board
        tag: A string that holds the abbreviation of the board
        slug: A string that holds the slug URL snippet for readable URLs
        lastUpdated: A DateTime that stores the last time a post was contributed
                    to.
    """

    name = models.CharField(max_length=50, db_index=True)
    tag = models.CharField(max_length=10, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'board' 
        verbose_name_plural = 'boards'

    @property
    def latestPost(self):
        """
            This function is to receives the latest post from a specific board

            Args:
                self: current instance of that object
        """
        return self.thread.order_by('created').last()



class Thread(models.Model):
    """
        Class for the Thread Object

        Attributes:
            title: a string that holds the title of the thread
            slug: a string that holds the slug URL snippet for the Thread
            created: a datetime object that holds the time the Thread was created
            poster: the User Object that created the Thread
            board: a reference to the board model where the Thread will be posted
            replyCount: an integer that holds the amount of times the thread
                             has been replied to
            views: an integer that holds the amount of times the Thread has
                       been viewed by other users
            imageCount: an integer that shows how many images are within the
                            thread repliess
            latestReplyTime: a Datetime object that holds the last time a user
                             has replied to the thread
    """
    title = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True, blank=True)
    created = models.DateTimeField(auto_now = True)
    board = models.ForeignKey(Board, related_name='threads', on_delete=models.CASCADE)
    replyCount = models.PositiveIntegerField(default = 0)
    views = models.PositiveIntegerField(default = 0)
    imageCount = models.PositiveIntegerField(default = 0)
    latestReplyTime = models.DateTimeField(auto_now = True)

    @property
    def tag(self):
        return self.board.tag

    @property
    def image(self):
        return self.posts.order_by('created').first().image

    @property
    def blurb(self):
        return self.posts.order_by('created').first().message[:50]

    @property
    def poster(self):
        return self.posts.order_by('created').first().poster.name

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created'] 
        verbose_name = 'thread'
        verbose_name_plural = 'threads'
    


    def save(self, **kwargs):
        """
            This function overrides the save function of the
            thread model in order to uppdate latestReply and numberOfReplies
        """
        if not self.pk:
            slug = self.title
            slug = slug.lower()
            slug = slug.replace(" ", "-")
            self.slug = slug

        if self.pk:
            self.latestReplyTime = datetime.now

        super(Thread, self).save(**kwargs)


class Post(models.Model):
    """
        A class for Post object
        Attributes:
            message: the content within the post itself (the text)
            created: a date time object that stored the time of the post's creation
            poster: the user who created the post
            thread: a foreign key to a thread object where the post has been made
            image: an imagefield for posts.
    """
    title = models.TextField(default = '')
    message = models.TextField(default = '')
    created = models.DateTimeField(auto_now = True)
    poster = models.ForeignKey(Profile, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='postImages/',
                              blank=True,
                              default='',
                              null=True)

    def __str__(self):
       return self.message


    class Meta:
        ordering = ['created']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def save(self, **kwargs):
        if not self.pk:
            self.thread.replyCount = self.thread.replyCount + 1
            self.thread.save()

        if not self.thread:

        super(Post, self).save(**kwargs)
