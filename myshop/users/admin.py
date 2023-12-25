from django.contrib import admin
from .models import Profile
# Register your models here.


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'phone_number')
    search_fields = ('user__username', 'user__email', 'phone_number')
