from atexit import register
import re
from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)
