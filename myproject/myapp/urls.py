from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_person, name='add_person'),
    path('edit/<str:pk>/', views.edit_person, name='edit_person'),
    path('delete/<int:pk>/', views.delete_person, name='delete_person'),
]
