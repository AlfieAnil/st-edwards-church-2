from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test', views.test),
    path('contact-us', views.contact_us, name='contact-us'),
    path('parish-hub', views.parish_hub, name='parish-hub'),
    path('calendar', views.calendar, name='calendar'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('baptism', views.baptism, name='baptism')
]