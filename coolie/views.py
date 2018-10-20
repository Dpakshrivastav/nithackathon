from django.views import generic
from django.shortcuts import render, redirect
from .form import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Employee, Booking, Location, Rate, Available
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'coolie/signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'coolie/home.html')


def reserve(request):
    railway = request.POST.get('station')
    railid = Location.objects.filter(railwayStation=railway).values_list('id', flat=True)
    coolieId = Employee.objects.filter(id__in=railid).values_list('id', flat=True)
    coolie = Employee.objects.all()
    avail = Available.objects.filter(id__in=coolieId)
    context = {'coolie': coolie, 'mylist': zip(coolie, avail)}
    return render(request, 'coolie/list.html', context)


def destination(request):
    stations = Location.objects.all()
    return render(request, 'coolie/destination.html', { 'stations' : stations })


def profile(request, coolie_id):
    coolie = Employee.objects.filter(id=coolie_id)
    return render(request, 'coolie/profile.html', {'coolie':coolie})
