from django.urls import path
from .views import index, home, aboutus, platform, team, contactus

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('aboutus/', aboutus, name='aboutus'),
    path('platform/', platform, name='platform'),
    path('team/', team, name='team'),
    path('contactus/', contactus, name='contactus'),
]
