from django.contrib import admin
from .models import Profile, BookShopUser


@admin.register(BookShopUser)
class BookShopAdmin(admin.ModelAdmin):
    list_display = ("email", "date_joined", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "date_joined")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "age", "profile_money", "user_email")
    list_filter = ("age",)
    search_fields = ("first_name", "last_name", "user__email")
    readonly_fields = ("profile_money",)
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'age', 'user')
        }),
        ('Финансова Информация', {
            'fields': ('profile_money',),
            'classes': ('collapse',)
        }),
        ('Профилна Снимка', {
            'fields': ('profile_picture',),
            'classes': ('collapse',)
        }),
    )

    def full_name(self, obj):
        return obj.full_name

    full_name.short_description = "Пълно име"

    def user_email(self, obj):
        return obj.user.email

    user_email.short_description = "Потребителски имейл"
