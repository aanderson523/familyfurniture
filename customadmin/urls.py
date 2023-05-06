from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.admin_login, name='login'),
    path("ct-admin/", admin.site.urls),

]