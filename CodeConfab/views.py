from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from CodeConfab.models import Profile, Language,Post,FriendRequest,Poke, Prompt,Resources,Comment,Reply
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from CodeConfab.forms import PostForm,CommentForm,ReplyForm
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator



# Create your views here.
@login_required
def home(request):
    if request.user.is_authenticated:
        post_list = Post.objects.filter(language__id__in = request.user.language_set.values_list('id',flat = True)).order_by('-created')
        paginator = Paginator(post_list, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        resources = Resources.objects.all()
        return render (request, 'Confab/home.html', {'posts':posts, 'resources':resources})
    else:
        return render(request, 'Confab/index.html')

def index(request):
    if request.user.is_authenticated:
        post_list = Post.objects.filter(language__id__in = request.user.language_set.values_list('id',flat = True)).order_by('-created')
        paginator = Paginator(post_list, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        resources = Resources.objects.all()
        return render (request, 'Confab/home.html', {'posts':posts, 'resources':resources})
    else:
        return render(request, 'Confab/index.html')

@login_required
def post(request, user):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit= False)
            post.user_id = request.user.id
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Successful, your post has beed added, you can poke a friend or two if you want them to help.')
            return redirect(reverse('confab:home'))
    else:
        header = 'New Post'
        form = PostForm
        return render(request, 'Confab/new2.html', {'form':form, 'header':header})


@login_required
def postdetail(request,user,pk, postslug):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user_id = request.user.id
            comment.post_id = post.id
            comment.save()    
            messages.add_message(request, messages.SUCCESS, 'Successful, Comment Added.')               
            return redirect(reverse('confab:post_detail', args=[user, pk, postslug] ))            
    else:
        form = CommentForm(request.POST)
        post = Post.objects.get(pk = pk)

        return render(request ,'Confab/post_detail.html', { 'post':post, 'form':form})

@login_required
def commentdetail(request, user, slug, com):
     if request.method == 'POST':
        comment = Comment.objects.get(pk = com )
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit = False)
            reply.user_id = request.user.id
            reply.comment_id = com
            reply.save()                   
            messages.add_message(request, messages.SUCCESS, 'Successful, Reply added.')
            return redirect(reverse('confab:comment_detail', args=[user, slug, com] ))  
                  
     else:
         form = ReplyForm(request.POST)
         comment = Comment.objects.get(pk = com)

         return render(request ,'Confab/comment_detail.html', { 'comment':comment, 'form':form})



@receiver(post_save, sender = User)
def createuserprofile(sender, **kwargs):
    if kwargs['created']:
        user_profile =Profile.objects.create(user = kwargs['instance'], date_joined = timezone.now())


class LanguageView(DetailView):
    model = Language
    template_name = 'Confab/language.html'

@login_required
def ConnectionsView(request, user):
    users = Profile.objects.exclude(user = request.user).exclude(user__is_staff = True).exclude(user__in =request.user.profile.friend.values_list('user',flat = True))
    
    return render( request, 'Confab/connections.html', {'users':users})

@login_required
def Connect(request, user):
    if request.method == 'POST':
        user = get_object_or_404(User, username = user)  
        friend_request, created = FriendRequest.objects.get_or_create(
        sender = request.user,
        receiver = user
        )
        messages.add_message(request, messages.SUCCESS, 'Successful, a connection request has been sent to'+ ' ' + user.username)
        return redirect(reverse('account:pub_profile', args = [user]))

@login_required
def DeleteRequest(request, reqid):
    if request.method =='POST':
        user = get_object_or_404(User, id = request.user.id)  
        con_request = FriendRequest.objects.get(id = reqid)
        con_request.delete()
        messages.add_message(request, messages.SUCCESS, 'Successful, friend request deleted.')
        return redirect(reverse('confab:connections', args = [user]))

@login_required 
def  AcceptRequest(request, user, id):
    if request.method == 'POST':
        con_request = FriendRequest.objects.get(id = id)
        users = User.objects.exclude(username = 'admin').exclude(username = request.user.username)    
        requests = FriendRequest.objects.filter(receiver_id = request.user.id)
        sender_user = get_object_or_404(User, username = user) 
        sender = Profile.objects.get(user_id = sender_user.id)
        receiver = Profile.objects.get(user_id = request.user.id)
        receiver.friend.add(sender)
        con_request.delete()
        messages.add_message(request, messages.SUCCESS, 'Successful, you are now connected to'+ ' ' + sender.user.username)
        return redirect(reverse('confab:connections', args = [request.user]), kwargs=[users, requests]) 

@login_required
def DeleteConnection(request, friend):
    if request.method == 'POST':
        friend = Profile.objects.get(id = friend)  
        receiver = Profile.objects.get(user_id = request.user.id)
        receiver.friend.remove(friend)
        user = friend.user
        messages.add_message(request, messages.SUCCESS, 'Successful, you are no longer connected to'+ ' ' + user.username)
        return redirect(reverse('account:pub_profile', args = [user]))


@login_required
def PokeList(request,slug, post):
    post = get_object_or_404(Post, id = post)

    return render(request, 'Confab/poke_list.html', {'post':post})

@login_required
def PromptList(request,slug, post):
    post = get_object_or_404(Post, id = post)
    return render(request, 'Confab/prompt_list.html', {'post':post}) 

@login_required
def PokeFriend(request, post):
    if request.method == 'POST':        
        user_list = request.POST.getlist("connections")
        users = User.objects.filter(username__in = user_list)
        post = get_object_or_404(Post, id = post)
        for pokee in users:
            poke, created = Poke.objects.get_or_create(
                poker = request.user,
                poked = pokee,
                post = post
            )
            messages.add_message(request, messages.SUCCESS, 'Poke Successful, your friends will be notified')
        return redirect(reverse('confab:home'))

@login_required
def PromptFriend(request, post):
    if request.method == 'POST':
        user_list = request.POST.getlist("connections")
        users = User.objects.filter(username__in = user_list)
        post = get_object_or_404(Post, id = post)
        for promptee in users:
            prompt, created = Prompt.objects.get_or_create(
                prompter = request.user,
                prompted = promptee,
                post = post
            )
            messages.add_message(request, messages.SUCCESS, 'Prompt Successful, your friends will be notified')
        return redirect(reverse('confab:home'))

@login_required
def SeePoke(request, id):
    if request.method == 'POST':
        poke = get_object_or_404(Poke, id = id)
        if poke.seen:
            return redirect(reverse('confab:post_detail', args=[poke.post.user, poke.post.pk, poke.post.slug]))
        else:
            poke.seen = True
            poke.save()
            return redirect(reverse('confab:post_detail', args=[poke.post.user, poke.post.pk, poke.post.slug]))

@login_required
def SeePrompt(request, id):
    if request.method == 'POST':
        prompt = get_object_or_404(Prompt, id = id)
        if prompt.seen:
            return redirect(reverse('confab:post_detail', args=[prompt.post.user, prompt.post.pk, prompt.post.slug]))
        else:
            prompt.seen = True
            prompt.save()
            return redirect(reverse('confab:post_detail', args=[prompt.post.user, prompt.post.pk, prompt.post.slug]))

@login_required
def Notifications(request, user):
    return render(request, 'Confab/notifications.html')


def Help(request):
    return render(request, 'Confab/help.html')


def About(request):
    return render(request, 'Confab/about.html')



def ResourcesView(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        if title != '':
            resource_list = Resources.objects.filter(title__contains = title)
        else:
            resource_list =[]
    else:
        resource_list = Resources.objects.filter(language__id__in = request.user.language_set.values_list('id',flat = True))
    
    paginator = Paginator(resource_list, 10)
    page = request.GET.get('page')
    resources = paginator.get_page(page)
    return render(request, 'Confab/resources.html', {'resources':resources})

def SuggestFriends(request, user):
    Suggestions = User.objects.filter(language__id__in = request.user.language_set.values_list('id',flat = True)).exclude(username = request.user).distinct().exclude(id__in = request.user.profile.friend.values_list('user_id',flat = True))
    return render(request, 'Confab/Suggestions.html', {'Suggestions':Suggestions})

def FindFriends(request, user):
    if request.method == 'POST':
        username=request.POST.get('username')
        if username != '':
            Suggestions = User.objects.filter(username__contains = username).exclude(is_staff = True)
        else:
            Suggestions = None
        
    return render(request, 'Confab/Friendresults.html', {'Suggestions':Suggestions})


    
def Contact(request):
    return render(request, 'Confab/contact.html')
    






