from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Root URL mapped to home view
]
