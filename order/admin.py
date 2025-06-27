# from django.contrib import admin
# from .models import CartItem, Favorite

# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product_display', 'quantity', 'added_at')
#     list_filter = ('user', 'content_type')
#     search_fields = ('user__username',)

#     def product_display(self, obj):
#         return str(obj.product)
#     product_display.short_description = "Product"


# @admin.register(Favorite)
# class FavoriteAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product_display', 'added_at')
#     list_filter = ('user', 'content_type')
#     search_fields = ('user__username',)

#     def product_display(self, obj):
#         return str(obj.product)
#     product_display.short_description = "Product"

from django.contrib import admin
from .models import CartItem, Favorite, Order, OrderItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_display', 'quantity', 'added_at')
    list_filter = ('user', 'content_type')
    search_fields = ('user__username',)

    def product_display(self, obj):
        return str(obj.product)
    product_display.short_description = "Product"


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_display', 'added_at')
    list_filter = ('user', 'content_type')
    search_fields = ('user__username',)

    def product_display(self, obj):
        return str(obj.product)
    product_display.short_description = "Product"


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'quantity')
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'payment_method', 'delivery_method', 'created_at', 'total_price')
    list_filter = ('status', 'delivery_method', 'payment_method')
    search_fields = ('user__username', 'email', 'phone')
    inlines = [OrderItemInline]