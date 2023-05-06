from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('selection/', views.shopping, name='shopping'),
]