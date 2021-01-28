from django.db import models
from django.core.validators import FileExtensionValidator
from account.models import Profile

# Create your models here.

class Post(models.Model):
    content = models.TextField(blank=False,  max_length=1000)
    images = models.ImageField(upload_to='posts', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    liked = models.ManyToManyField(Profile, default=None, related_name='likes', blank=True )
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')


    def __str__(self):
        return str(self.content)

    

    def num_likes(self):
        return  self.liked.all().count()   

    #num of comment

    def num_comments(self):
        return self.comment_set.all().count()

    class Meta:
        ordering = ('-created',)    


#for comment model


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.pk)

LOVE_CHOCIES =(
    ('like', 'Like'),
    ('unlike', 'Unlike'),

)

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LOVE_CHOCIES, max_length=8, )
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}" 