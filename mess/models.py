from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class messagerecord(models.Model):
    msg_sender = models.ForeignKey(User,on_delete = models.CASCADE , related_name='msg_sender')
    msg_reciever = models.ForeignKey(User,on_delete=models.CASCADE , related_name='msg_reciever')
    created_at = models.DateTimeField(auto_now_add=True)
    msg_content = models.TextField()