from django.shortcuts import render
from .models import FilterDemo


# Create your views here.

def sample_view(request):
    Filter_data = FilterDemo.objects.all()
    return render(request, 'temp_app/home.html', {'Filter_data': Filter_data})
