from django.urls import path
from .views import index, home, aboutus, platform

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('aboutus/', aboutus, name='aboutus'),
    path('platform/', platform, name='platform'),
]
