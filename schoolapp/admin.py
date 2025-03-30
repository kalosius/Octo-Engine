from django.contrib import admin
from . models import ContactMessage

# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'preferred_method', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('preferred_method', 'created_at')
    ordering = ('-created_at',) 

admin.site.register(ContactMessage, ContactMessageAdmin)
