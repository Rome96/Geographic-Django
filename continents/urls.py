from django.contrib import admin
from django.urls import path
from continents.views import ContinentsView,ContinentDetailView

app_name = 'continents'

urlpatterns = [
    path("<int:pk>/", ContinentDetailView.as_view(), name="detail"),
    path("", ContinentsView.as_view(), name="home"),
]