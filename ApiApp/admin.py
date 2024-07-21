from django.contrib import admin
from ApiApp.models import *
# Register your models here.


class TaskListView(admin.ModelAdmin):
    model = Tasks
    list_display = ["Task_title", "slug"]


admin.site.register(Tasks, TaskListView)
