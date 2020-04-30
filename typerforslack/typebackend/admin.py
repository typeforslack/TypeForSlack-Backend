from django.contrib import admin
from .models import TypingRecord

# Register your models here.

class TypingAdmin(admin.ModelAdmin):
    list_display=['user_id','speed','typeddate']

admin.site.register(TypingRecord,TypingAdmin)