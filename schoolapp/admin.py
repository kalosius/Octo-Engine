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





# Customize the admin site
admin.site.site_header = "ST.Francis School Admin"
admin.site.site_title = "ST.Francis Admin Portal"
admin.site.index_title = "Welcome to ST.Francis Administration"
