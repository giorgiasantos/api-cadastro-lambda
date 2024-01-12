from django.urls import path
from .import views

urlpatterns = [
    path('pessoas/', views.pessoa_list)
]