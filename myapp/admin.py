from django.contrib import admin
from .models import Account, Sumrush, Google

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'numbers')

@admin.register(Sumrush)
class SumrushAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword', 'difficulty', 'volume', 'cpc', 'account')
    list_filter = ('keyword', 'difficulty', 'volume', 'cpc')
@admin.register(Google)
class GoogleAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword')
