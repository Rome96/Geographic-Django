from django import forms

class RegisterForm(forms.Form):
	first_name = forms.CharField(label='First name')
	last_name = forms.CharField(label='Last name')