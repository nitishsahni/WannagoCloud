from django.contrib import admin

from .models import Riserva, DRaaS, IaaS, Subscriptions


class RiservaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price_dollars', 'price_aed', 'selling_price')


class DRaaSAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'cost_price', 'selling_price')


class IaaSAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'cost_price', 'selling_price')


class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'selling_price')



admin.site.register(Riserva, RiservaAdmin)
admin.site.register(DRaaS, DRaaSAdmin)
admin.site.register(IaaS, IaaSAdmin)
admin.site.register(Subscriptions, SubscriptionsAdmin)
