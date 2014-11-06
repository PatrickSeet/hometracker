from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.conf import settings
from hometracker.forms import EmailUserCreationForm, PropertyForm, PropertyNotesForm
from hometracker.models import Property
from hometracker.models import PropertyNotes
from geolocation.google_maps import GoogleMaps
from json import encoder
import json

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            html_content = '<h2>Thanks {} {}for signing up!</h2> <div>I hope you enjoy using our site</div><div>Signed up on {}'.format(
                user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("login")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


def faq(request):
    return render(request, 'faq.html')


def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'registration/profile.html')


@login_required()
def properties(request):
    json.encoder.FLOAT_REPR = lambda o: format(o, '.6f')
    properties = Property.objects.all()

    cords_list = []

    for i in properties:
        cords_list.append(i.xcoordinate)
        cords_list.append(i.ycoordinate)

    cords_json = json.dumps(cords_list)

    data = {"properties": properties, "cords_json": cords_json}
    return render(request, "properties/properties.html", data)


@login_required()
def new_property(request):
    # If the user is submitting the form
    if request.method == "POST":

        # Get the instance of the form filled with the submitted data
        # form = PropertyForm(request.POST)
        form = PropertyForm(request.POST, request.FILES)
        # Django will check the form's validity for you
        if form.is_valid():

            # Saving the form will create a new Property object
            if form.save():
                data = form.cleaned_data
                property_address = data['address']
                google_maps = GoogleMaps(api_key='AIzaSyDlHBtlOb1-JpUPZ8CHAZqaNha6Uw_l_ow')
                location_info = google_maps.query(location=property_address)
                location_info = location_info.first()
                Property.objects.filter(address=property_address).update(xcoordinate=location_info.lat)
                Property.objects.filter(address=property_address).update(ycoordinate=location_info.lng)

                # After saving, redirect the user to add propertynotes
                return redirect("new_propertynotes")

    # Else if the user is looking at the form page
    else:
        form = PropertyForm()

    data = {'form': form}

    return render(request, "properties/add_property.html", data)
    # return render(request, "properties/test_add_property.html", data)


@login_required()
def view_property(request, property_id):
    property = Property.objects.get(id=property_id)
    notes = PropertyNotes.objects.get(property_id=property_id)
    percentage_over = round((float(property.soldprice - property.askingprice) / float(property.askingprice)) * 100)
    beat_by = property.soldprice - property.offeredpricce
    x = property.xcoordinate
    y = property.ycoordinate

    data = {"property": property, "notes": notes, "percentage_over": percentage_over, "beat_by": beat_by,
            "x": x, "y": y}

    return render(request, "properties/view_property.html", data)


@login_required()
def edit_property(request, property_id):
    # Similar to the the detail view, we have to find the existing genre we are editing
    property = Property.objects.get(id=property_id)

    # We still check to see if we are submitting the form
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            if form.save():
                return redirect("/property/{}".format(property_id))

    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = PropertyForm(instance=property)
    data = {"property": property, "form": form}
    return render(request, "properties/edit_property.html", data)


@login_required()
def new_propertynotes(request):
    # If the user is submitting the form
    if request.method == "POST":

        # Get the instance of the form filled with the submitted data
        form = PropertyNotesForm(request.POST)

        # Django will check the form's validity for you
        if form.is_valid():

            # Saving the form will create a new Genre object
            if form.save():
                # After saving, redirect the user back to the index page
                return redirect("/properties")

    # Else if the user is looking at the form page
    else:
        form = PropertyNotesForm()
    data = {'form': form}

    return render(request, "properties/add_propertynotes.html", data)


@login_required()
def edit_propertynotes(request, property_id):
    # Similar to the the detail view, we have to find the existing genre we are editing
    propertynotes = PropertyNotes.objects.get(property_id=property_id)

    # We still check to see if we are submitting the form
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = PropertyNotesForm(request.POST, instance=propertynotes)
        if form.is_valid():
            if form.save():
                return redirect("/property/{}".format(property_id))

    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = PropertyNotesForm(instance=propertynotes)
    data = {"propertynotes": propertynotes, "form": form}
    return render(request, "properties/edit_propertynotes.html", data)


@login_required()
def delete_property(request, property_id):
    propertynotes = PropertyNotes.objects.get(property_id=property_id)
    property = Property.objects.get(id=property_id)
    propertynotes.delete()
    property.delete()


    return redirect("/properties/")