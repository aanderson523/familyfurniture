from django.db import models
from django.db import models
from django.conf import settings
from django.utils.timezone import now
# Create your models here.

class Instock(models.Model):

     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
     available = models.IntegerField(default=0)
     ordered= models.BooleanField(default=False)
