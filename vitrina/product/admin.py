from django.contrib import admin
from .models import Offer, Lead


# Register your models here.

class LeadAdmin(admin.ModelAdmin):
    list_display = ['id','datetime', 'name', 'phone', 'offer', 'ip']
    list_display_links = ['id', 'name', 'phone']
    list_filter = ['offer']


admin.site.register(Offer)
admin.site.register(Lead,LeadAdmin)
