from django.contrib import admin
from .models import User

class AdminUser(admin.ModelAdmin):
    list_display = ("firstname" , "lastname" , "joined_date",)

admin.site.register(User , AdminUser)