from django.urls import path

from myuser import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('company', views.company, name='company'),
]
