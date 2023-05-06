from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    birth_date = models.DateField()
    address = models.CharField(max_length=250)
    
    def __str__(self):
        return self.user.username