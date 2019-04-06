from django.urls import path
from api.views import search
urlpatterns = [
    path('search/', search, name="search"),
]

