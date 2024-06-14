from django.shortcuts import get_object_or_404, render
from .models import Customer, Product
#from django.shortcuts import HttpResponse

# Create your views here.
'''def index (request):
  return HttpResponse("<h1> Using Shortcuts. My first webpage with PythonDjango!</h1>")'''
def home(request):
    context = {}
    return render(request, 'myplpecom/home.html', context)

def product_list(request):
  products = Product.objects.all()
  context = {
    'products': products
  }
  return render(request, 'myplpecom/product_list.html', context)

def product_detail(request, pk):
  product = get_object_or_404(Product, pk=pk)
  context = {
    'product': product
  }
  return render (request, 'myplpecom/product_detail.html', context)

def customer_list(request):
  customers = Customer.objects.all()
  context = {
    'customers': customers
  }
  return render(request, 'myplpecom/customer_list.html', context)

def customer_detail(request, pk):
  customer = get_object_or_404(Customer, pk=pk)
  context = {
    'customer': customer
  }
  return render (request, 'myplpecom/customer_detail.html', context)