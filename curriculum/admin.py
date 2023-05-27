from django.contrib import admin
from .models import Standard, Subject, Lesson, Comment, Reply, Courses

# Register your models here.


admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Courses)