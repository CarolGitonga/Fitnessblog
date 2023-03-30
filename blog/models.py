from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

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
    slug = models.SlugField(max_length =250, unique_for_date='publish')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length =2, choices=Status.choices, default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    objects = models.Manager()# The default manager
    published = PublishedManager()# Our custom managerf
    tags = TaggableManager()

    class Meta:# this class defines metadata for the model
         ordering = ['-publish']#ordering attribute tells Django to sort results by the publish field
         indexes = [#This option allows database indexes for your model
              models.Index(fields=['-publish']),
         ]

    def __str__(self):
         return self.title
    
    def get_absolute_url(self):#builds URL dynamically using the URL name defined in the URL patterns.
         return reverse('blog:post_detail', args=[self.publish.year,
                                                  self.publish.month,
                                                  self.publish.day,
                                                  self.slug])#parameters of the canonical URL for blog posts to match the new URL parameters.

class Comment(models.Model):
     post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
     name = models.CharField(max_length=80)
     email = models.EmailField()
     body = models.TextField()
     created = models.DateField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)
     active = models.BooleanField(default=True)

     class Meta:
          ordering = ['created']
          indexes = [
               models.Index(fields=['created']),
          ]
     def __str__(self):
          return f'Comment by {self.name}  on {self.post }'