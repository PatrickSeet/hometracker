from django.forms import ModelForm
import hometracker
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hometracker.models import Shopper
from hometracker.models import Property
from hometracker.models import PropertyNotes


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Shopper
        fields = ("username", "first_name", "last_name", "phone", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Shopper.objects.get(username=username)
        except Shopper.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        # won't show x,y cords to user to fill out
        # fields = ("mlsid", "address", "numofbdrms", "numofbthrms", "numofmaster", "sqfootage", "lotsize",
        # "askingprice", "offeredpricce", "soldprice", "frontyard", "backyard", "propertytype",
        # "prop_image", "shopper")
        exclude = ('xcoordinate', 'ycoordinate',)


class PropertyNotesForm(ModelForm):
    class Meta:
        model = PropertyNotes