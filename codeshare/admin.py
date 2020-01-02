from django.contrib import admin

# Register your models here.
from codeshare.models import Problem, Code, Comment

admin.site.register(Problem)
admin.site.register(Code)
admin.site.register(Comment)
