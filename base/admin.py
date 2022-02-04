from django.contrib import admin
from .models import TrendyProducts
# Register your models here.

class TrendyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'offeramt', 'img')


admin.site.register(TrendyProducts,TrendyAdmin)
