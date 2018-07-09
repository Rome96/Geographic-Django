from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class ContinentsView(TemplateView):
	template_name = 'continents/continents.html'

	def get_context_data(self, *args, **kwargs):

		america = {'name': 'américa', 'translation': 'america', 'color': '#F7DC6F'}
		antartida = {'name': 'antártida', 'translation': 'antartica', 'color': '#2874A6'}
		europa = {'name': 'europa', 'translation': 'europe', 'color': '#E74C3C'}
		africa = {'name': 'africa', 'translation': 'africa', 'color': '#2ECC71'}
		oceania = {'name': 'oceania', 'translation': 'oceania', 'color': '#A93226'}
		asia = {'name': 'asia', 'translation': 'asia', 'color': '#8E44AD'}

		continents = [
			america,
			antartida,
			europa,
			africa,
			oceania,
			asia
		]

		return {'continents': continents}