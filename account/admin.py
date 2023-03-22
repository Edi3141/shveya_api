from django.contrib import admin

from account.models import CustomUser, Personal, UserProfile

admin.site.register(CustomUser)
admin.site.register(Personal)
admin.site.register(UserProfile)

