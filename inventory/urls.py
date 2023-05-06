from .views import item_list
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app_name = 'store'

urlpatterns = [
    path('', item_list, name='item-list')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
