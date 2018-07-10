from django.urls import path
from countries.views import CountryDetailView, CountryIdDetailView

urlpatterns = [
    path('<int:id>', CountryIdDetailView.as_view(), name="country_id_detail"),
    path('<code>', CountryDetailView.as_view(), name="country_code_detail")
    
]
