from django.contrib import admin
from .models import *
# Register your models here.


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'time_create', 'is_published')


admin.site.register(People, PeopleAdmin)

