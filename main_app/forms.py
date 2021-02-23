from django.forms import ModelForm
from .models import Plant, Watering


class WateringForm(ModelForm):
    class Meta:
        model = Watering
        fields = ['date']


class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'description', 'waterAmount', 'lighting']
