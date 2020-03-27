from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView

app_name = 'account'

urlpatterns = [

    path('registration/' , views.register.as_view(), name = 'register'),
    path('logout/', views.Logout.as_view(), name = 'logout'),
    path('login/' , views.login.as_view(), name = 'login'),
    path('password/change/',views.PasswordChange.as_view(), name = 'password_change'),
    path('password/change/done/',views.PasswordChangDone.as_view(), name = 'password_change_done'),
    path('reset-password', views.passwordreset.as_view(), name = 'reset_password'),
    path('password/reset/done', views.passwordresetdone.as_view(), name = 'password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>', views.confirmpasswordreset.as_view(), name = 'password_reset_confirm'),
    path('password-reset/complete', views.passwordresetcomplete.as_view(), name = 'password_reset_complete'),
    path('profile/',views.profileview, name = 'profile'),
    path('<str:user>/profile/public',views.Publicprofile, name = 'pub_profile'),
    path('profile/work/information/edit', views.UpdateWorkInfo, name = "work_edit"),
    path('profile/personal_information/edit', views.UpdatePersonalinfo, name = 'edit_pinfo'),
    path('profile/contact_information/edit', views.UpdateContatctinfo, name = 'edit_cinfo'),    
    path('profile/acheivements/edit', views.UpdatAcheiveInfo, name = 'edit_ainfo'),
    path('profile/other_information/edit', views.UpdateOtherInfo, name = 'edit_oinfo'),
    path('profile/education_information/edit', views.UpdateEducationInfo, name = 'edu_edit'),
    path('profile/user/story/edit', views.UpdateAboutInfo, name = 'about_edit'),
    path('profile/user/edit/language/add', views.AddLanguages, name = 'lang_add'),
    path('profile/user/edit/language/remove', views.RemoveLanguages, name = 'lang_remove'),
    path('user/resources/add', views.ResourceAdd , name = 'add_resource'),  
    path('user/resources/<int:resourceid>/delete', views.ResourceDelete , name = 'rem_resource'),   
    path('user/profile/picture/add', views.UploadProfilepic , name = 'add_pic')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
