from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    contact_no = models.PositiveIntegerField(default=91)
    nick_names = models.CharField(max_length=200, default=True)
    frequently_uttered_words = models.CharField(max_length=300, default = True)
    striking_features = models.CharField(max_length=300,null=True)
    about_me = models.CharField(max_length=300,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'



# Create your models here.

class Comments(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	comment = models.TextField(default="write comment")
	posted_by = models.CharField(max_length=200, null = True)
	posted_on = models.DateTimeField(default=timezone.now, null=True)