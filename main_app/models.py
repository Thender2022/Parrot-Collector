from django.db import models
from django.urls import reverse
from datetime import date


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Jacket(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jackets_detail', kwargs={'pk': self.id})

class Parrot(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    jackets = models.ManyToManyField(Jacket)

    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'parrot_id':self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0],
      )

    parrot = models.ForeignKey(
        Parrot, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']