from django.contrib import admin
from CodeConfab.models import Profile, Language, Resources,Post,Comment,Reply

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    exclude = 'date_joined', 'friend'
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Language)
admin.site.register(Resources)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)