from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from social_django.urls import urlpatterns as social_urls
from django.urls import path, include

urlpatterns = [
    path('', views.signup, name='signup'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('social-auth/', include('social_django.urls', namespace='social')),

]