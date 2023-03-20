from django.contrib import admin

from account.models import CustomUser, Personal

admin.site.register(CustomUser)
admin.site.register(Personal)

