from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, DriverProfile, PassengerProfile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role')
    
    # Extend the fieldsets to include the custom field 'role'
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    
    # Optionally, you can also add 'role' to add_fieldsets for new users.
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number', 'vehicle_model', 'seats_available')
    search_fields = ('user__username', 'license_number', 'vehicle_model')


@admin.register(PassengerProfile)
class PassengerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')
    search_fields = ('user__username',)

