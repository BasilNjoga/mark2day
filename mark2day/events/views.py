from django.shortcuts import render

# Create views are here

def home(request):
    return render(request, 'home.html', {})
