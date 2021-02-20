from django.db import models
from django.urls import reverse
# Create your models here.

LIGHTING = (
    ('SD', 'Shade'),
    ('LL', 'Low Light'),
    ('DS', 'Direct sun')
)

WATERAMOUNT = (
    ('E', 'Everyday'),
    ('W', 'Weekly'),
    ('R', 'Rarely')
)


class Plant(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    waterAmount = models.CharField(
        max_length=20,
        choices=WATERAMOUNT,
        default=WATERAMOUNT[0][0])
    lighting = models.CharField(
        max_length=20,
        choices=LIGHTING,
        default=LIGHTING[0][0])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plant_detail', kwargs={'plant_id': self.id})


class WateringDate(models.Model):
    date = models.DateField()

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Watered on {self.date}"
