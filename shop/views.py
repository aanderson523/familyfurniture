from django.shortcuts import render

# Create your views here.
def shop(request):
    return render(request, 'shop/shop.html')

def shopping(request):
    return render(request, 'selection/instock.html')