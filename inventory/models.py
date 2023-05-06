from django.db import models
from django.conf import settings
from django.utils.timezone import now
# Create your models here.

User = settings.AUTH_USER_MODEL

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('stale', 'Stale'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('instore pickup', 'Instore Pickup'),
    ('refunded', 'Refunded'),

)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    item_type = models.CharField(max_length=100)
    item_img = models.ImageField(upload_to='images/', default='', null=True, blank=True)
    inventory = models.IntegerField(default=0)
    def __str__(self):
        return self.title




class OrderItem(models.Model):
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='images', default='', null=True, blank=True)
    
    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES,default='created')
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.username
