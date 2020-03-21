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
            tag: A string that holds the abbreviation of the board (index in the db)
            lastUpdated: A DateTime that stores the last time a post was contributed
                    to.
            nextBid: An integer field used to count the amount of posts on a board
                    this number will be passed on to our posts to have that relative
                    ID that will be displayed on the forum.
    """

    name = models.CharField(max_length=50, db_index=True, unique=True)
    tag = models.CharField(primary_key=True, max_length=4, db_index=True)
    nextBid = models.PositiveIntegerField(default = 0)
    activeThreadCount = models.PositiveIntegerField(default = 0)
    nsfw = models.BooleanField(default = False)

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
        return self.threads.order_by('created').last()

    @property
    def activeThreads(self):
        """
            This function returns back a list of active threads from a specific board

            Args
                self: current instance of the object
        """
        return self.threads.filter(status = 'active')

    @property
    def lockedThreads(self):
        """
            This function returns back a list of locked threads from a specific board

            Args:
                Self: current instance of the object
        """
        return self.threads.filter(status = 'locked')

    @property
    def archivedThreads(self):
        """
            This function returns back a list of archived threads from a specific board

            Args:
                self: current instance of the object
        """
        return self.threads.filter(status = 'archived')

    def archiveLeastActiveThread(self):
        """
            This function doesn't return anything. It only updates the least active thread
            and changes its status to archived, this is so we can make more room for active
            threads.

            Args:
                self: current instance of the object.

        """
        laThread = self.threads.order_by('latestReplyTime').first()
        laThread.status = ('archived')
        laThread.save()



class Thread(models.Model):
    """
        Class for the Thread Object

        Attributes:
            title: a string that holds the title of the thread
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
            image: Image field that holds an image that will be displayed with
                    the thread
            bid: reference to the first post in the bid
    """
    ACTIVE = 'active'
    LOCKED = 'locked'
    ARCHIVED = 'archived'

    STATUSES = [
        (ACTIVE, 'active'),
        (LOCKED, 'locked'),
        (ARCHIVED, 'archived')
    ]


    title = models.CharField(max_length=250, db_index=True)
    created = models.DateTimeField(auto_now = True)
    board = models.ForeignKey(Board, related_name='threads', on_delete=models.CASCADE)
    replyCount = models.PositiveIntegerField(default = 0)
    views = models.PositiveIntegerField(default = 0)
    imageCount = models.PositiveIntegerField(default = 0)
    updated = models.DateTimeField(auto_now = True)
    poster = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(blank = True, default='',null=True)
    status = models.CharField(max_length = 20, choices = STATUSES, default = ACTIVE)


    @property
    def tag(self):
        return self.board.tag


    @property
    def blurb(self):
        return self.posts.order_by('created').first().message[:50]

    @property
    def bid(self):
        return self.posts.order_by('created').first().bid


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
            self.status = 'active'
            if self.board.activeThreadCount >= 5:
                self.board.archiveLeastActiveThread()
            else:
                self.board.activeThreadCount += 1
                self.board.save()


        super(Thread, self).save(**kwargs)


class Post(models.Model):
    """
        A class for Post object
        Attributes:
            title: Hidden text field, this is only used in the creation of
                a post that will be the head of a thread.
            message: the content within the post itself (the text)
            created: a date time object that stored the time of the post's creation
            poster: the user who created the post
            thread: a foreign key to a thread object where the post has been made
            image: an imagefield for posts.
            bid: A integer field that holds the post ID, which is relative to each board
                    (making it not a unique ID throughout the entire database, but only for
                    a specific board)
    """
    title = models.TextField(default = '', blank = True)
    bid = models.PositiveIntegerField(default = 0)
    message = models.TextField(default = '')
    created = models.DateTimeField(auto_now = True)
    board = models.ForeignKey(Board, on_delete = models.CASCADE)
    poster = models.ForeignKey(Profile, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE, blank = True, null = True)
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
            self.bid = self.board.nextBid
            self.board.nextBid = self.board.nextBid + 1
            self.board.save()

            try:
                self.thread.replyCount = self.thread.replyCount + 1
                if self.image:
                        self.thread.imageCount = self.thread.imageCount + 1
                self.thread.latestReplyTime = datetime.now
                self.thread.save()

            except:
                newThread = Thread(title = self.title, board = self.board, poster = self.poster, image = self.image)
                newThread.save()
                self.thread = newThread
                if self.image:
                    self.thread.save()
                    self.thread.imageCount = self.thread.imageCount + 1

        super(Post, self).save(**kwargs)
