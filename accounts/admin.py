from django.contrib import admin
from accounts.models import CustomUser, extra_user_info, BlockList

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'create_on']


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'ip', 'browser']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(extra_user_info,UserInfoAdmin)
admin.site.register(BlockList)
