from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


app_name = 'confab'

urlpatterns = [
    path('' , views.index, name = 'index'),
    path('home/' , views.home, name = 'home'),
    path('resources/' , views.ResourcesView, name = 'resources'),
    path('help/' , views.Help, name = 'help'),
    path('about/' , views.About, name = 'about'),
    path('contact/' , views.Contact, name = 'contact'),
    path('languages/<int:pk>/details', views.LanguageView.as_view(), name = 'lang_detail'),
    path('<str:user>/post/new/' , views.post, name = 'post'),
    path('<str:user>/posts/<int:pk>/<str:postslug>' , views.postdetail, name = 'post_detail'),
    path('<str:user>/<str:slug>/comments/<int:com>', views.commentdetail, name = 'comment_detail'),
    path('<str:user>/Connections/' , views.ConnectionsView, name = 'connections'),
    path('<str:user>/connection/request/send', views.Connect, name ='connect'),
    path('connection/request/<reqid>/delete', views.DeleteRequest, name= 'delete_request'),
    path('connection/request/<id>/<str:user>/accept', views.AcceptRequest, name= 'accept_request'),
    path('connections/<friend>/delete', views.DeleteConnection, name= 'disconnect'),
    path('<post>/<slug>/action/poke', views.PokeList, name = 'poke_list'),
    path('<post>/<slug>/action/prompt', views.PromptList, name = 'prompt_list'),
    path('<post>/connection/poke', views.PokeFriend, name= 'poke'),
    path('<post>/connection/prompt', views.PromptFriend, name= 'prompt'),
    path('<id>/prompt/see/', views.SeePrompt, name = 'see_prompt'),
    path('<id>/poke/see/', views.SeePoke, name = 'see_poke'),
    path('<user>/notifications', views.Notifications, name= 'notify'),
    path('<user>/Connection-Suggestions', views.SuggestFriends, name= 'suggest'),
    path('<user>/Connections/Find', views.FindFriends, name= 'find'),
    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)