from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event
from .forms import VenueForm

# Create views are here

# Takes you to the list of all events
def all_events(request):
    event_list = Event.objects.all()

    return render(request, 'events/current_events.html',
     {
        'event_list': event_list
     })

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = False
    form = VenueForm
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})



# View to the admin page
def my_admin(request):

    return redirect("/admin/")

# View to the main page
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Basil"
    month = month.capitalize()
    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create a calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number )
    # Get current year
    now = datetime.now()
    current_year = now.year 

    # Get current time
    time = now.strftime('%I:%M %p')
    return render(request, 'events/home.html', {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })
