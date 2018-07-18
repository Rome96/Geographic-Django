from django.db import models

# Create your models here.
class Continent(models.Model):
	name = models.CharField(max_length=100)
	translate = models.CharField(max_length=100)
	color = models.CharField(max_length=100)

	def __str__ (self):
		return self.name