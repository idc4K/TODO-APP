
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.todo, name="accueil"),
    path('mod/<str:pk>/', views.modifier, name="modifier"),
   
]
