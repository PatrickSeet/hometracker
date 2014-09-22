from django.contrib import admin
from hometracker.models import Property
from hometracker.models import PropertyNotes
from hometracker.models import Shopper

# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyNotes)
admin.site.register(Shopper)