from django.urls import path, include
from . import views


app_name = 'front'



urlpatterns = [
    path('', include('main.dashboard.urls')),
]