from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.


class Problem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('problems_detail', kwargs={'pk': self.id})


class Plant(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    water_amount = models.IntegerField()
    lighting = models.CharField(max_length=100)
    problems = models.ManyToManyField(Problem)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plant_detail', kwargs={'plant_id': self.id})

#Function to check days since watering 
    def needs_water(self):
        return self.watering_set.filter(date=date.today()).count() >= 1 
        # watering_date = Watering.objects.first()

        # last_watering = watering_date.date.day
        # print(last_watering)
        # day = date.today().day
        # days_since_watering = day - self.water_amount
        # print(days_since_watering)
        # if days_since_watering <= last_watering:
        #     return True
        # else:
        #     return False
        





class Watering(models.Model):
    date = models.DateField('watering date')

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"
    class Meta:
        ordering = ['-date']