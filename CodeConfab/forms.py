from django.forms import ModelForm
from django import forms
from .models import Resources,Profile,Comment, Post,Reply



class ResourceForm(ModelForm):

    class Meta:
        model = Resources
        exclude = {'user'}

class ProfilePicForm(ModelForm):

    class Meta:
        model = Profile
        fields = {'profile_picture'}

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        exclude = {'slug', 'user','created'}

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        exclude = {'post','user', 'created'}

class ReplyForm(ModelForm):

    class Meta:
        model = Reply
        fields = {'text'}