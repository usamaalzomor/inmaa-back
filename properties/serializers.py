# properties/serializers.py

from rest_framework import serializers
from .models import Property, PropertyImage, Amenity, Category, PropertyType
from core.models import City, State

# Serializer for listing (only the required fields)
class PropertyListSerializer(serializers.ModelSerializer):
    # Return only the name of each related field
    city = serializers.CharField(source='city.name', read_only=True)
    state = serializers.CharField(source='state.name', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    property_type = serializers.CharField(source='property_type.name', read_only=True)

    class Meta:
        model = Property
        fields = [
            'id',
            'operation',
            'price',
            'area',
            'rooms',
            'bathrooms',
            'city',
            'state',
            'category',
            'property_type',
        ]

# Serializers for nested related objects
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ['id', 'name']

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name']

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image', 'is_main']

# Serializer for detailed view (all fields)
class PropertyDetailSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    state = StateSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    property_type = PropertyTypeSerializer(read_only=True)
    # Many-to-many and reverse relations:
    amenities = AmenitySerializer(many=True, read_only=True)
    images = PropertyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        # Using '__all__' to include every field on the model
        fields = '__all__'
