from django.contrib import admin
from .models import Partner, User

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'company_name', 'contact_name', 'email')

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_active', 'is_staff')


admin.site.register(Partner, PartnerAdmin)
admin.site.register(User, UserAdmin)