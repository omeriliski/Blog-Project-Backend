from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

def user_directory_path(instance,filename):
    return 'blog/{0}/{1}'.format(instance.author.id,filename)

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path,default='default.jpg')
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(blank=True,unique=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    #if user is deleted, comment will be deleted
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    post = models.ForeignKey(Post,on_delete=CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username
        
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    post = models.ForeignKey(Post,on_delete=CASCADE)

    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    post = models.ForeignKey(Post,on_delete=CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username