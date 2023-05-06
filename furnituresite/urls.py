"""furnituresite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inventory import views
from django.contrib.auth import views as auth_views
from social_django.urls import urlpatterns as social_urls

urlpatterns = [
   
    path('', include('store.urls')),
    path('admin/dashboard/', include('login.urls')),
    path('admin/', include('login.urls')),
    path("ct-admin/", admin.site.urls),
    path('shop/', include('shop.urls')),
    path('login/', include('login.urls')),
    path('logout/', include('logout.urls')),
    path('financing/', include('financing.urls')),
    path('members/', include('members.urls')),
    path('accounts/', include('allauth.urls')),
    path('item_list/<int:items_id>', include('selection.urls')),
    path('selection/', include('selection.urls')),
    path('accounts/', include('allauth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('social-auth/', include('social_django.urls', namespace='social')),
  
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
