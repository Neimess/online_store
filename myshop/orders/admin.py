from django.contrib import admin

# Register your models here.

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['products']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'postal_code',
                    'created', 'updated', 'paid', 'get_user']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

    @admin.display(ordering='users', description='User')
    def get_user(self, obj):
        return obj.user
