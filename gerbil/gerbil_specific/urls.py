from django.urls import path
from . import views

urlpatterns = [
    path('gerbil/<int:id>/', views.intro, name='intro'),
]

