from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
	template_name = 'countries/home.html'
	#def get(self, request, *args, **kwargs):
	   # return render(request, "countries/home.html")
   

class ListView(TemplateView):
	template_name = 'countries/list.html'