from django.shortcuts import render

# Create your views here.

def financing(request):
    return render(request, 'financing.html')