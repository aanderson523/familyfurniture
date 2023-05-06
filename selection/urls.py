from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib import admin
from shop.views import shop
from django.conf import settings


urlpatterns = [
    path('shop', views.shop, name='shopping'),
    path('shopping/', views.items, name='shopping')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

