from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Problem
from .forms import WateringForm
# Create your views here.
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

@login_required
def index(request):
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/index.html', {'plants': plants})

@login_required
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    potential_problems = Problem.objects.exclude(id__in = plant.problems.all().values_list('id'))
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', {
        'plant': plant,
        'watering_form': watering_form,
        'available_problems': potential_problems
    })

@login_required
def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('plant_detail', plant_id=plant_id)

@login_required
def assoc_problem(request, plant_id, problem_id):
    Plant.objects.get(id=plant_id).problems.add(problem_id)
    return redirect('plant_detail', plant_id=plant_id)


class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ['name', 'description', 'water_amount', 'lighting']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ['description', 'water_amount', 'lighting']


class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'




class ProblemList(LoginRequiredMixin, ListView):
    model = Problem

class ProblemDetail(LoginRequiredMixin, DetailView):
    model = Problem

class ProblemCreate(LoginRequiredMixin, CreateView):
    model = Problem
    fields = '__all__'

class ProblemUpdate(LoginRequiredMixin, UpdateView):
    model = Problem
    fields = ['name', 'description']

class ProblemDelete(LoginRequiredMixin, DeleteView):
    model = Problem
    success_url = '/problems/'