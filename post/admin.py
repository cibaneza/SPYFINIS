from django.contrib import admin
from .models import PostModel
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('profe', 'date_created')

admin.site.register(PostModel, PostModelAdmin)