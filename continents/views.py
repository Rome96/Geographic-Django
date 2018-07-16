from django.shortcuts import render
from django.http import HttpResponse
from .models import Continent
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class ContinentsView(ListView):
    template_name="continents/home.html"
    model = Continent

class ContinentDetailView(DetailView):
	template_name="continents/detail.html"
	model = Continent 