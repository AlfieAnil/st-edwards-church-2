from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name="login"),
    path('create-user', views.registerPage, name="create-user"),
    path('create-priest-message', views.createPriestMessage, name="create-priest-message"),
    path('upload-newsletter', views.NewsletterUpload, name='upload-newsletter')
]