from django.urls import path
from . import views

##defining the paths
urlpatterns =[

    path('Hello/', views.Hello, name= 'Hello'),

]