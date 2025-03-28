from django.contrib import admin
from .models import PostModel, Comment

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']

admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Comment)

# Register your models here.
