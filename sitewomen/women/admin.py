from django.contrib import admin
from women.models import Post, Comment, Tags
from mptt.admin import MPTTModelAdmin

admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Comment, MPTTModelAdmin)