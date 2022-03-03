from django.contrib import admin
from .models import FilterDemo
# Register your models here.

class FilterAdmin(admin.ModelAdmin):
    list_display = ['name','subject','dept','date']

admin.site.register(FilterDemo,FilterAdmin)