from django.db import models
from django.core.validators import MinValueValidator
from core.models import City, State

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class PropertyType(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='p_types/')
    
    class Meta:
        unique_together = ('name', 'category')
    
    def __str__(self):
        return f"{self.category} - {self.name}"

class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='p_amenities/')
    
    def __str__(self):
        return self.name

class Property(models.Model):
    USAGE_CHOICES = [
        ('residential', 'سكنية'),
        ('commercial', 'تجارية'),
        ('industrial', 'صناعية'),
        ('agricultural', 'زراعية'),
        ('administrative', 'إدارية'),
        ('touristic', 'سياحية'),
    ]

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('rented', 'Rented'),
        ('sold', 'Sold'),
    ]

    OPERATION_CHOICES = [
        ('for_rent', 'For Rent'),
        ('for_sale', 'For Sale'),
    ]

    # Core Information
    title = models.CharField(max_length=50, null=False, blank=False, default="property")
    property_type = models.ForeignKey(PropertyType, on_delete=models.PROTECT)
    usage_type = models.CharField(max_length=20, choices=USAGE_CHOICES,
                                default='residential', null=False, blank=False,
                                help_text="Select the type of usage (commercial, industrial, residential)"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available',
        help_text="Indicates whether the property is available, booked, or finished (rented/sold)"
    )

    operation = models.CharField(max_length=15, choices=OPERATION_CHOICES)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    
    # Specifications
    area = models.FloatField(validators=[MinValueValidator(0)])
    furniture_included = models.BooleanField(default=False)
    floor = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    
    # Location
    city = models.ForeignKey(City, on_delete=models.PROTECT, default=1)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    # Additional Info
    description = models.TextField(blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    year_built = models.PositiveIntegerField(null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['property_type', 'furniture_included']),
            models.Index(fields=['price']),
            models.Index(fields=['rooms'])
        ]

    def __str__(self):
        return f"{self.property_type} @ {self.city.name}"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='properties/')
    is_main = models.BooleanField(default=False)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['property'],
                condition=models.Q(is_main=True),
                name='unique_main_image'
            )
        ]
    
    def __str__(self):
        return f"Image for {self.property}"