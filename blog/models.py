from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class PublishedManager(models.Manager):
     def get_queryset(self):
          return super().get_queryset()\
          .filter(status=Post.Status.PUBLISHED)
     

class Post(models.Model):
    
    class Status(models.TextChoices):#enumerate class Status by subclassing models.TextChoices.  
         DRAFT = 'DF','Draft'#available choices for the post status are DRAFT and PUBLISHED.
         PUBLISHED = 'PB','Published'#Their respective values are DF and PB, and their labels or readable names are Draft and Published.

    title = models.CharField(max_length =250)
    body = models.TextField()
    slug = models.SlugField(max_length =250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length =2, choices=Status.choices, default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    objects = models.Manager()# The default manager
    published = PublishedManager()# Our custom managerf

    class Meta:# this class defines metadata for the model
         ordering = ['-publish']#ordering attribute tells Django to sort results by the publish field
         indexes = [#This option allows database indexes for your model
              models.Index(fields=['-publish']),
         ]

    def __str__(self):
         return self.title
