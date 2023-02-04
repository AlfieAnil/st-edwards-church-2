from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test', views.test),
    path('contact-us', views.contact_us, name='contact-us'),
    path('parish-hub', views.parish_hub, name='parish-hub'),
    path('calendar', views.calendar, name='calendar'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('baptism', views.baptism, name='baptism'),
    path('funeral', views.funeral, name='funeral'),
    path('anointing-of-the-sick', views.anointing, name='anointing'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('holy-communion', views.holy_communion, name='holy-communion'),
    path('holy-orders', views.holy_orders, name='holy-orders'),
    path('marriage', views.marriage, name='marriage'),
    path('reconciliation', views.reconciliation, name='reconciliation'),
    path('about-us', views.about_us, name='about-us'),
    path('schools', views.schools, name='schools'),
    path('liturgy', views.liturgy, name='liturgy')
]