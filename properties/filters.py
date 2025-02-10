# properties/filters.py

import django_filters
from properties.models import Property

class PropertyFilter(django_filters.FilterSet):
    operation = django_filters.ChoiceFilter(choices=Property.OPERATION_CHOICES)
    category_id = django_filters.NumberFilter(field_name='property_type__category__id')
    property_type_id = django_filters.NumberFilter(field_name='property_type__id')
    furniture_included = django_filters.BooleanFilter(field_name='furniture_included')
    country_id = django_filters.NumberFilter(field_name='city__state__country')
    state_id = django_filters.NumberFilter(field_name='city__state')
    city_id = django_filters.NumberFilter(field_name='city__id')
    floor = django_filters.NumberFilter(field_name='floor', lookup_expr='exact')
    rooms = django_filters.NumberFilter(field_name='floor', lookup_expr='exact')
    bathrooms = django_filters.NumberFilter(field_name='floor', lookup_expr='exact')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    area_min = django_filters.NumberFilter(field_name='area', lookup_expr='gte')
    area_max = django_filters.NumberFilter(field_name='area', lookup_expr='lte')

    class Meta:
        model = Property
        fields = ['category_id', 'property_type_id', 'country_id', 'city_id', 'state_id',
                    'price_min', 'price_max', 'area_min', 'area_max', 'operation'
                 ]
