from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    title =models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(blank = True)
    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length = 1024)

class Friends(models.Model):
    person1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person1')
    person2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person2')

class Friendrequests(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE , related_name='sender')
    reciever = models.ForeignKey(User , on_delete = models.CASCADE , related_name= 'reciever')