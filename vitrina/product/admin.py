from django.contrib import admin
from .models import Offer, Lead, AdcomboOffer, LeadRockOffer, KmaOffer, Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'desc']
    list_display_links = list_display

class LeadAdmin(admin.ModelAdmin):
    list_display = ['id','datetime', 'name', 'phone', 'offer', 'ip']
    list_display_links = ['id', 'name', 'phone']
    list_filter = ['offer']

class AdcomboOfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','offer_id', 'base_url', 'country_code']
    list_display_links = list_display
class LeadRockOfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','flow_url']
    list_display_links = list_display

class KmaOfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','channel', 'country']
    list_display_links = list_display



admin.site.register(Offer)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AdcomboOffer, AdcomboOfferAdmin)
admin.site.register(LeadRockOffer, LeadRockOfferAdmin)
admin.site.register(Lead,LeadAdmin)
admin.site.register(KmaOffer, KmaOfferAdmin)

