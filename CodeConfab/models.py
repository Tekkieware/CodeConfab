from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    dob = models.DateField('Date of birth', null = True, blank = True)
    gender = models.CharField(max_length = 6, null = True)
    about = models.CharField(max_length = 200 ,null = True, blank = True)
    education = models.CharField('What schools have you attended?',max_length = 200, null = True, blank = True)
    religion = models.CharField(max_length = 20 , null = True, blank = True)
    nationality = models.CharField(max_length = 50 , null = True, blank = True)
    state_of_origin = models.CharField('State of Origin',max_length = 50, null = True, blank = True)
    hometown = models.CharField(max_length = 50, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    address = models.CharField(max_length = 50, null = True, blank = True)
    work = models.CharField('Tell us about your work', max_length =100, null = True, blank = True)
    acheivements = models.CharField ('Successful work done in programming', max_length = 200, null = True, blank = True)
    phone = models.CharField('Phone Number', max_length = 20, null = True, blank = True)
    profile_picture = models.ImageField(upload_to = 'profile_pictures/', null = True, blank = True) 
    date_joined = models.DateField(null = True, blank = True) 
    friend = models.ManyToManyField("self", blank = True) 
    
    def __str__(self):
        return self.user.username
    


class Language(models.Model):
    users = models.ManyToManyField(User, blank = True)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    user_base = models.IntegerField(null = True, blank= True)
    notable_use = models.CharField(max_length = 100, null = True, blank = True)
    


    def __str__(self):
        return self.name



class Resources(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    link  = models.URLField('Add a link to your resource',null = True, blank = False)
    pdf = models.FileField('Add pdf if any',upload_to = 'resources/pdfs/', null = True, blank =True)
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    language = models.ForeignKey(Language, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Post(models.Model):
    language = models.ForeignKey(Language, on_delete = models.CASCADE)
    user =models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    slug = models.SlugField(unique = False)
    description = models.TextField('Describe your errors:')
    code = models.TextField('Paste code here:')
    created = models.DateTimeField(null = True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.created = timezone.now()
        super().save(*args, **kwargs)
        
        

    
class Comment(models.Model):
    user =models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    text = models.TextField('Give opinion:', null = True, blank=True)
    code = models.TextField('Fix Code:', null = True, blank=True)
    created = models.DateTimeField()


    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):        
        self.created = timezone.now()
        super().save(*args, **kwargs)

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE)
    text = models.TextField('Reply', null= False, blank= False)
    created = models.DateTimeField()

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        self.created = timezone.now()
        super().save(*args, **kwargs)

class FriendRequest(models.Model):
    sender = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'sent_requests')
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'received_requests')
    date_sent = models.DateField()

    def __str__(self):
        return self.sender

    def save(self, *args, **kwargs):        
        self.date_sent = timezone.now()
        super().save(*args, **kwargs)


class Prompt(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    prompter = models.ForeignKey(User, on_delete =models.CASCADE, related_name = 'sent_prompts')
    prompted = models.ForeignKey(User, on_delete =models.CASCADE, related_name = 'received_prompts')
    date_sent = models.DateField(default = timezone.now)
    seen = models.BooleanField(default =False)

    class Meta:
        ordering = ['-date_sent']


class Poke(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    poker = models.ForeignKey(User, on_delete =models.CASCADE, related_name = 'sent_pokes')
    poked = models.ForeignKey(User, on_delete =models.CASCADE, related_name = 'received_pokes')
    date_sent = models.DateField(default = timezone.now)
    seen = models.BooleanField(default =False)
    
    class Meta:
        ordering = ['-date_sent']

   






