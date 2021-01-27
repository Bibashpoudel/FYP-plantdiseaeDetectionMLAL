from django.db import models

from django.contrib.auth.models import User

from .utils import get_random_code

from django.template.defaultfilters import slugify

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank = True)
    last_name = models.CharField(max_length=200, blank =True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", max_length=300)
    email = models.EmailField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatar.ping', upload_to='avatars/')

    friends = models.ManyToManyField(User, blank =True, related_name='friends')

    slug = models.SlugField(unique=True, blank = True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # grabing reiend request from 

    #get freind list name
    def get_friends(self):
        allFreind = self.friends.all()

        return allFreind

    #get number of freind
    def get_friends_no(self):
        allFreindno = self.friends.all().count()

        return allFreindno


    #get number of post
    def get_posts_no(self):
        nopost = self.posts.all().count()  

        return nopost  

    #get posts list name
    def get_posts(self):
        posts = self.posts.all()

        return posts

    #get all user post 
    def get_all_user_post(self):
        allposts = self.posts.all()

        return allposts  

    #get likes number
    def get_likes_given_no(self):
        likes = self.like.set.all()
        total_likes = 0
        for item in likes:
            if item.value == 'love':
                total_likes +=1 

        return total_likes

    #get recive love
    def get_likes_recevie_no(self):
        post = self.posts.all()
        total_likes = 0
        for item in post:
            total_likes += item.liked.all().count()

        return total_likes




    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%y')}"

    def save(self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
            to_slug =  slugify(str(self.first_name) + " " + str(self.last_name))
            ex = Profile.objects.filter(slug= to_slug).exists()
            while ex:
                to_slug = slugify(to_slug +" "+ str(get_random_code()))
                ex = ex = Profile.objects.filter(slug= to_slug).exists() 
        else:
            to_slug = str(self.user)
        self.slug = to_slug    
        super().save(*args, **kwargs) 


STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)


class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=9, choices=STATUS_CHOICES)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
