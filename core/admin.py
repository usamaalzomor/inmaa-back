from django.contrib import admin
from core.models import Service
from .models import Service, Country, State, City


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'state_code', 'country')
    list_filter = ('country',)
    search_fields = ('name', 'state_code')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_code', 'state')
    list_filter = ('state',)
    search_fields = ('name', 'city_code')
