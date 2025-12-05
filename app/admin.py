from django.contrib import admin
from .models import Lottery


@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'lottery_number', 'aimag', 'sum', 'horoo', 'status')
    search_fields = ('phone_number', 'lottery_number', 'aimag', 'sum', 'horoo', 'status')
    list_filter = ('aimag', 'sum', 'horoo', 'status')