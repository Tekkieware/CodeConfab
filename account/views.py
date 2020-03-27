from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from django.contrib.auth.views import (LoginView, PasswordResetView, 
PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView,
PasswordChangeDoneView,LogoutView)
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from CodeConfab.models import Profile, Language,Resources
from CodeConfab.forms import ResourceForm,ProfilePicForm
from django.contrib import messages
# Create your views here.




class register(generic.edit.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'account/register.html'
    success_url = '/accounts/login/'

class login(LoginView):
    template_name = 'account/login.html'

class passwordreset(PasswordResetView):
    template_name = 'account/password_reset_form.html'
    success_url = '/accounts/password/reset/done'
class passwordresetdone(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class confirmpasswordreset(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = '/accounts/password-reset/complete'

class passwordresetcomplete(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'

class PasswordChange(PasswordChangeView):
    template_name = 'account/password_change_form.html'
    success_url = '/accounts/password/change/done/'

class PasswordChangDone(PasswordChangeDoneView):
    template_name = 'account/passord_change_done.html'

class Logout(LogoutView):
    template_name = 'Confab/index.html'

@login_required
def profileview(request):    
    lang = Language.objects.exclude(users__id__contains =request.user.id)
    context = {'languages':lang}
    return render(request, 'account/profile.html', context)

@login_required
def Publicprofile(request, user):
    try:
        request.user.profile.friend.get(user__username = user)
        my_friend = True
    except:
        my_friend = False
    user = get_object_or_404(User, username = user)    
    context = {'user':user,'my_friend':my_friend}
    return render(request, 'account/public_profile.html', context)


def UpdatePersonalinfo(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)
        p = Profile.objects.get(user_id = request.user.id)
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        Gender = request.POST["gender"]
        Dob = request.POST["dob"]      
        user.first_name = fname
        user.last_name = lname
        if Dob:
            p.dob = Dob
        p.gender = Gender
        p.save()     
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Successful, your personal information has been updated.')
    return redirect(reverse('account:profile'))  

def UpdateContatctinfo(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)
        p = Profile.objects.get(user_id = request.user.id)
        nation = request.POST['nation']
        State = request.POST['state']
        Hometown = request.POST['hometown']
        City = request.POST['city']
        Homeaddress = request.POST['homeaddress']
        Email = request.POST['email']
        Phone = request.POST['phone']
        p.nationality = nation
        p.state_of_origin = State
        p.hometown = Hometown
        p.city = City
        p.address = Homeaddress
        user.email = Email
        p.phone = Phone
        p.save()
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Successful, your contact information has been updated.')
    return redirect(reverse('account:profile')) 

def UpdateWorkInfo(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)
        p = Profile.objects.get(user_id = request.user.id)
        Work = request.POST['work']
        p.work = Work
        p.save()
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Successful, your work information has been updated.')
        return redirect(reverse('account:profile'))  
    

def UpdatAcheiveInfo(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)
        p = Profile.objects.get(user_id = request.user.id)
        Acheive = request.POST['acheivements']
        p.acheivements = Acheive
        p.save()
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Successful, your acheivements have been updated.')
    return redirect(reverse('account:profile'))

def UpdateOtherInfo(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)
        p = Profile.objects.get(user_id = request.user.id)
        Rel = request.POST['religion']
        p.religion = Rel
        p.save()
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Successful, your other information has been updated.')
    return redirect(reverse('account:profile'))

def UpdateEducationInfo(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)
        p = Profile.objects.get(user_id = request.user.id)
        Edu = request.POST['education']
        p.education = Edu
        p.save()
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Successful, your academic information has been updated.')
        return redirect(reverse('account:profile'))  

def UpdateAboutInfo(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)
        p = Profile.objects.get(user_id = request.user.id)
        ab = request.POST['about']
        p.about = ab
        p.save()
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Successful, information about you have been.')
        return redirect(reverse('account:profile')) 

@login_required
def AddLanguages(request):
    if request.method == 'POST':
        langs = ""
        user = get_object_or_404(User, pk=request.user.id)
        language_list = request.POST.getlist('languages')
        languages = Language.objects.filter(pk__in = language_list)
        for lang in languages:
            user.language_set.add(lang)
            langs += str(lang) + '\n'          
        messages.add_message(request, messages.SUCCESS, 'Successful, The following programming languages have been added to your profile: \n' + langs)
        return redirect(reverse('account:profile'))

@login_required
def RemoveLanguages(request):
    if request.method == 'POST':
        langs = ""
        user = get_object_or_404(User, pk=request.user.id)
        language_list = request.POST.getlist('languages')
        languages = Language.objects.filter(pk__in = language_list)
        for lang in languages:
            user.language_set.remove(lang)
            langs += str(lang) + '\n'          
        messages.add_message(request, messages.SUCCESS, 'Successful, The following programming languages have been removed to your profile: \n' + langs)
        return redirect(reverse('account:profile'))

@login_required
def ResourceAdd(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        user = get_object_or_404(User, pk=request.user.id)
        if form.is_valid():
            resource = form.save(commit = False)
            resource.user_id = request.user.id
            resource.save()
            messages.add_message(request, messages.SUCCESS, 'Successful, your resource has been added.')
            return redirect(reverse('account:profile')) 
    else:
        form = ResourceForm()
        header = 'Upload Resource'
        return render(request, 'Confab/new.html', {'form':form, 'header':header})


def ResourceDelete(request, resourceid):      
    if request.method == 'POST':         
        resource = Resources.objects.get(pk = resourceid)
        resource.pdf.delete()
        resource.delete()                     
        messages.add_message(request, messages.SUCCESS, 'Successful, your resource has been deleted.')
    return redirect(reverse('account:profile')) 

def UploadProfilepic(request):
    if request.method == 'POST':
        form = ProfilePicForm(request.FILES, request.POST)        
        if form.is_valid():
            profile = Profile.objects.get(user_id = request.user.id)
            picture = request.FILES.get('profile_picture')
            if picture:
                profile.profile_picture.delete() 
                profile.profile_picture = picture
                profile.save()
                messages.add_message(request, messages.SUCCESS, 'Successful, your profile picture has been updated.')                                                   
            return redirect(reverse('account:profile')) 
    else:
        form = ProfilePicForm()
        header = 'Upload Profile Picture'
        return render(request, 'Confab/new.html', {'form':form, 'header':header})




    


        
            




       
        
            
            
    