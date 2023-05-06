from django.urls import path
from . import views

urlpatterns = [
    path('financing/', views.financing, name='financing')
]