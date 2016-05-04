from django.contrib import admin
from .models import Registration


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('birth_name', 'last_name', 'first_name')

admin.site.register(Registration, RegistrationAdmin)
