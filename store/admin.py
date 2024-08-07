from django.contrib import admin
from .models import Address, Category, Product, Cart, Order


# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "locality", "city", "state")
    list_filter = ("city", "state")
    list_per_page = 10
    search_fields = ("locality", "city", "state")


class ProductInline(admin.TabularInline):
    model = Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "category_image",
        "is_active",
        "is_featured",
        "updated_at",
    )
    list_editable = ("is_active", "is_featured")
    list_filter = ("is_active", "is_featured")
    list_per_page = 10
    search_fields = ("title", "description")
    readonly_fields = ["slug"]
    inlines = [ProductInline]


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "category",
        "product_image",
        "is_active",
        "is_featured",
        "updated_at",
    )
    list_editable = ("category", "is_active", "is_featured")
    list_filter = ("category", "is_active", "is_featured")
    list_per_page = 10
    search_fields = ("title", "category", "short_description")
    readonly_fields = ["slug"]


class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity", "created_at")
    list_editable = ("quantity",)
    list_filter = ("created_at",)
    list_per_page = 20
    search_fields = ("user", "product")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity", "status", "ordered_date")
    list_editable = ("quantity", "status")
    list_filter = ("status", "ordered_date")
    list_per_page = 20
    search_fields = ("user", "product")


admin.site.register(Address, AddressAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
