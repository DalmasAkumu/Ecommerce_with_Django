from django.shortcuts import render
from .models import Product
#from django.shortcuts import HttpResponse

# Create your views here.
'''def index (request):
  return HttpResponse("<h1> Using Shortcuts. My first webpage with PythonDjango!</h1>")'''

def product_list(request):
  products = Product.objects.all()
  context = {
    'products': products
  }
  return render(request, 'myplpecom/product_list.html', context)

