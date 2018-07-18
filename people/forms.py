from django import forms
from countries.models import Country
from people.models import Person

class RegisterForm(forms.Form):
	first_name = forms.CharField(label='First name')
	nacionality = forms.ModelMultipleChoiceField(queryset=Country.objects.all())
	father = forms.ModelChoiceField(queryset=Person.objects.all())