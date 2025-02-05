# properties/admin.py

from django.contrib import admin
from .models import Category, PropertyType, Amenity, Property, PropertyImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Define an inline admin for PropertyImage so you can manage images within the Property page
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'property_type', 'operation', 'price', 'area', 
        'rooms', 'bathrooms', 'city', 'state', 'category'
    )
    list_filter = ('operation', 'property_type', 'category', 'city', 'state')
    search_fields = ('description',)
    inlines = [PropertyImageInline]

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'is_main')
    list_filter = ('is_main',)
