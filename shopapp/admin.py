from django.contrib import admin
from .models import Brand, Color, Currency, Category, Product
from .models import User, Profile, Order, OrderItem, Review

# Models


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

    prepopulated_fields = {"slug": ("name",)}


class ColorAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

    prepopulated_fields = {"slug": ("name",)}


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

    prepopulated_fields = {"slug": ("name",)}


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "created_at",
                    "user", "first_name", "last_name",
                    "email", "address", "country",
                    "city", "zip_code")

    list_filter = ("status", "created_at")

    search_fields = ("first_name", "address")

    inlines = [OrderItemInline]


class ProductAdmin(admin.ModelAdmin):
    list_display = ("brand", "name", "category", "color", "price", "currency")

    prepopulated_fields = {"slug": ("name",)}


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "image")


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("product", "rating", "content", "created_by", "created_at")


admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewsAdmin)
