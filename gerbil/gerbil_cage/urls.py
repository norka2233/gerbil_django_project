from django.urls import pathfrom . import viewsurlpatterns = [    path('', views.index, name='index'),    path('success/', views.add_cage_form, name='add_cage_form'),    path('delete/<int:cage_id>', views.delete_cage_form, name='delete_cage_form'),]