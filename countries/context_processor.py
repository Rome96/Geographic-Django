def countries_data(request):
	colombia = {'name': 'colombia', 'code': 'Co'}
	usa = {'name': 'estados unidos', 'code': 'usa'}
	mexico = {'name': 'mexico', 'code': 'mx'}

	countries = [colombia, usa, mexico]
	return {'countries': countries}