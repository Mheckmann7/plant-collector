from django.db import models
from django.urls import reverse
# Create your models here.

# LIGHTING = (
#     ('SD', 'Shade'),
#     ('LL', 'Low Light'),
#     ('DS', 'Direct sun')
# )

# WATERAMOUNT = (
#     ('E', 'Everyday'),
#     ('W', 'Weekly'),
#     ('R', 'Rarely')
# )


class Problem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    days = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('problems_detail', kwargs={'pk': self.id})


class Plant(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    waterAmount = models.IntegerField()
    lighting = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plant_detail', kwargs={'plant_id': self.id})

    # def needs_water(self):
    #     return self.watering_set.filter(date=date.today()).count() >= self.waterAmount)


class Watering(models.Model):
    date = models.DateField('watering date')

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Watered on {self.date}"

    class Meta:
        ordering = ['-date']
