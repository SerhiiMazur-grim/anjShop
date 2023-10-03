from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()

@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'date_joined')


