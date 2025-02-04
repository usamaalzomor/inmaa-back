from django.db import models
from django.contrib.gis.db import models as gis_models
from core.utils import validate_boundary

class Service(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='service_icons/')

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    location = gis_models.MultiPolygonField(validators=[validate_boundary])

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    state_code = models.CharField(max_length=5)
    boundary = gis_models.MultiPolygonField(validators=[validate_boundary])

    def __str__(self):
        return f"{self.name}, {self.country.name}"

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city_code = models.CharField(max_length=5)
    boundary = gis_models.MultiPolygonField(validators=[validate_boundary]) 

    def __str__(self):
        return f"{self.name}, {self.state.name}"