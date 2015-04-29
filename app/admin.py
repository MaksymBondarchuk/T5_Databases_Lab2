from django.contrib import admin
from app.models import User, Bill, Time, Transaction

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment']
    ordering = ['name']
admin.site.register(User, UserAdmin)


class BillAdmin(admin.ModelAdmin):
    list_display = ['amount', 'average_amount_for_month']
    ordering = ['amount']
admin.site.register(Bill, BillAdmin)


class TimeAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'at_day_time']
    ordering = ['datetime']
admin.site.register(Time, TimeAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'bill', 'time']
    ordering = ['user']
admin.site.register(Transaction)#, TransactionAdmin)