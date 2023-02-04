from django.contrib import admin
from .models import School, Student


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_at', 'update_at')
    list_display_links = ('name', 'create_at', 'update_at')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'enrollment', 'school', 'create_at', 'update_at')
    list_display_links = ('name', 'school')


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
