from django.contrib import admin
from .models import Contact_person
# Register your models here.

class ContactpersonAdmin(admin.ModelAdmin):
    list_display= ('name','phone','email','photo')
    list_display_links = ('name',)
    search_fields = ('name','phone','email')

admin.site.register(Contact_person,ContactpersonAdmin)
