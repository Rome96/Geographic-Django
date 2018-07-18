from django.db import models

# Create your models here.
class Country(models.Model):
	CODES_CHOICES =(
	        ('CO', 'colombia'),
	        ('AR', 'argentina'),
	    )

	name = models.CharField(max_length=100)
	code = models.CharField(max_length=5)
	continent = models.ForeignKey('continents.Continent', on_delete=models.CASCADE)

	def __str__(self):
		return self.name
		