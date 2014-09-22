from django.contrib.auth.models import AbstractUser
from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.
class Property(models.Model):
    mlsid = models.IntegerField()
    address = models.CharField(max_length=100)
    askingprice = models.IntegerField()
    offeredpricce = models.IntegerField()
    soldprice = models.IntegerField()
    numofbdrms = models.IntegerField()
    numofbthrms = models.FloatField()
    numofmaster = models.IntegerField()
    frontyard = models.BooleanField(default=False)
    backyard = models.BooleanField(default=False)
    propertytype = models.CharField(max_length=100)

    def __unicode__(self):
        return self.address

class Shopper(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format should be: 650-111-2222")
    property = models.ManyToManyField(Property, related_name="property")

    def __unicode__(self):
        return self.first_name

class PropertyNotes(models.Model):
    roof = models.CharField(max_length=100)
    kitchen  = models.CharField(max_length=100)
    bathrooms  = models.CharField(max_length=100)
    frontyard  = models.CharField(max_length=100)
    backyard  = models.CharField(max_length=100)
    termite  = models.CharField(max_length=100)
    foundation  = models.CharField(max_length=100)
    neighborhood  = models.CharField(max_length=100)
    property = models.ForeignKey(Property, related_name='propertynotes')

    def __unicode__(self):
        return self.neighborhood

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()