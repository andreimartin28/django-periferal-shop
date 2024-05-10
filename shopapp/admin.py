from django.contrib import admin
from .models import Category, Product, User, Profile, Order, OrderItem, Review

# Models


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        "product", "rating", "content", "created_by", "created_at"
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name", "slug"
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name", "brand", "category",
        "color", "price"
    )

    list_filter = (
        "category", "brand", "color"
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user", "image"
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id", "status", "created_at",
        "user", "first_name", "last_name",
        "email", "address", "country",
        "city", "zip_code"
    )

    list_filter = (
        "status", "created_at"
    )

    search_fields = (
        "first_name", "address"
    )

    inlines = [OrderItemInline]


admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewsAdmin)
