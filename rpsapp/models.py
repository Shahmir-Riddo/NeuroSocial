from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import random
import uuid



# Create your models here.
class Profile(models.Model):
    
    # other fields
   
    p_id = models.IntegerField(null=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, null=True)
    avatar = models.ImageField(upload_to='media/images', blank=True)
    cover = models.ImageField(upload_to='media/images', blank=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)



   
class Post(models.Model):
    
    # other fields
    id = models.UUIDField( primary_key = True,
         default = uuid.uuid4,
         editable = False)
    username = models.CharField(default='Anonymous User', max_length=50)
    caption = models.CharField(max_length=3000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(default='4c50870fef410d14ff495ea1f532565a.jpg',upload_to='post/photo', null=True)
    no_of_likes = models.IntegerField(null=True)
  

    def __str__(self):
        return self.caption


class LikePost(models.Model):
    post_id = models.UUIDField()
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100, null=True)
    user = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user

class Comment(models.Model):
    username = models.CharField(default='Anonymous User', max_length=50)
    pid = models.CharField(max_length=1000, null=True)
    username = models.CharField(default='Anonymous User', max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    text = models.CharField(max_length=300)
