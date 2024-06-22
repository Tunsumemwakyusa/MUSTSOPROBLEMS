from django.urls import path
from .views import index, home, aboutus

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('aboutus/', aboutus, name='aboutus'),
]
