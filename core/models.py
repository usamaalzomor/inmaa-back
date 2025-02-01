from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='service_icons/')

    def __str__(self):
        return self.name