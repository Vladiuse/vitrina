from django.contrib import admin
from .models import Offer, Lead, AdcomboOffer, KmaOffer, Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'ru_name', 'desc', 'slug', ]
    list_display_links = list_display
    prepopulated_fields = {"slug": ("name",)}


class OfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'public', 'name', 'slug', 'old_price', 'price', 'doctor_rank',
                    'price', 'low_price', 'mini_land', ]
    list_display_links = list_display
    prepopulated_fields = {"slug": ("name",)}


class LeadAdmin(admin.ModelAdmin):
    list_display = ['id', 'datetime', 'name', 'phone', 'offer', 'ip']
    list_display_links = ['id', 'name', 'phone']
    list_filter = ['offer']


class AdcomboOfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'offer_id', 'base_url', 'country_code']
    list_display_links = list_display


class KmaOfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'channel', 'country']
    list_display_links = list_display


admin.site.register(Offer, OfferAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AdcomboOffer, AdcomboOfferAdmin)
admin.site.register(Lead, LeadAdmin)
admin.site.register(KmaOffer, KmaOfferAdmin)
