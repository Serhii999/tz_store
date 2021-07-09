from django.contrib import admin
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'email']

    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(StoreUser)
admin.site.register(Categories)
admin.site.register(Product)


