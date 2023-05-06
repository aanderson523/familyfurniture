from django.contrib import admin
from . models import Item, OrderItem, Order
# Register your models here.


admin.site.register(OrderItem)
admin.site.register(Order)

class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    
admin.site.register(Item, ItemAdmin)

