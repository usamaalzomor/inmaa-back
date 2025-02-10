from rest_framework import serializers
from .models import Property, PropertyImage, Amenity, Category, PropertyType
from core.models import City, State


class PropertyListSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name', read_only=True)
    state = serializers.CharField(source='city.state.name', read_only=True)
    category = serializers.CharField(source='property_type.category.name', read_only=True)
    property_type = serializers.CharField(source='property_type.name', read_only=True)
    image = serializers.SerializerMethodField()
    is_in_wishlist = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = [
            'id',
            'image',
            'title',
            'operation',
            'price',
            'area',
            'floor',
            'rooms',
            'bathrooms',
            'city',
            'state',
            'category',
            'property_type',
            'usage_type',
            'status',
            'is_in_wishlist',
            ]

    def get_is_in_wishlist(self, obj):
        return False
    
    def get_image(self, obj):
        image = obj.images.filter(is_main=True).first()
        return image.image.url if image else None

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
    city = property_type = serializers.CharField(source='city.name')
    state = property_type = serializers.CharField(source='city.state.name')
    category = serializers.CharField(source='property_type.category.name')
    property_type = serializers.CharField(source='property_type.name')
    # Many-to-many and reverse relations:
    amenities = AmenitySerializer(many=True, read_only=True)
    images = PropertyImageSerializer(many=True, read_only=True)
    is_in_wishlist = serializers.CharField(read_only=True)

    class Meta:
        model = Property
        fields = ['id', 'images', 'title', 'category', 'property_type', 'operation', 'price',
                'area', 'furniture_included', 'floor', 'rooms', 'bathrooms', 'usage_type',
                'amenities', 'description', 'year_built', 'city', 'state', 'status',
                'is_in_wishlist', 'latitude', 'longitude'
                ]

    def get_is_in_wishlist(self, obj):
        return False