from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant
from .forms import WateringForm, PlantForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})


def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    plant_form = PlantForm()
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', {
        'plant': plant,
        'plant_form': plant_form,
        'watering_form': watering_form,
    })


def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('plant_detail', plant_id=plant_id)


class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'


class PlantUpdate(UpdateView):
    model = Plant
    fields = ['description', 'waterAmount', 'lighting']


class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'
