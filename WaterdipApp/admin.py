from django.contrib import admin
from .models import TaskTable
# Register your models here.
@admin.register(TaskTable)
class TaskTableAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_completed')
    search_fields = ('id','title')