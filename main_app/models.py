from django.db import models
from django.urls import reverse
from datetime import date

WEARS = (
	('SU', 'Sunday'),
	('M', 'Monday'),
	('TU', 'Tuesday'),
	('W', 'Wednesday'),
	('TH', 'Thursday'),
	('F', 'Friday'),
	('SA', 'Saturday'),
)


# Create your models here.
class Box(models.Model):
	color = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('boxes_detail', kwargs={'pk': self.id})



class Sneaker(models.Model):
	name = models.CharField(max_length = 100)
	year = models.CharField(max_length = 100)
	designer = models.CharField(max_length = 250)

	boxes = models.ManyToManyField(Box)

	def __str__(self):
		return self.name


class Wearing(models.Model):
	date = models.DateField('Date Worn')
	wear = models.CharField(
		max_length = 2,
		choices=WEARS,
		default=WEARS[5][0]
		
		)

	sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.get_wear_display()} on {self.date}"

class Meta:
	ordering = ['-date']
