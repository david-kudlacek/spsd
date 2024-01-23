from django.contrib import admin

# Register your models here.
from .models import DataInsert
from .models import Post

admin.site.register(DataInsert)
admin.site.register(Post)
