from django.contrib import admin
from . models import ContactMessage, SeniorOne

# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'preferred_method', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('preferred_method', 'created_at')
    ordering = ('-created_at',) 

admin.site.register(ContactMessage, ContactMessageAdmin)


class SeniorOneAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'elective', 'sex')
    search_fields = ('first_name', 'last_name', 'elective')
    list_filter = ('sex', 'first_name', 'last_name')
    ordering = ('-first_name',) 

admin.site.register(SeniorOne, SeniorOneAdmin)
