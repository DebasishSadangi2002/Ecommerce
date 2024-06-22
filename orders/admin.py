from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id', 'user', 'status', 'created_at']
    list_filter = ['status', 'created_at']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
