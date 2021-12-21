from django.shortcuts import render
from .models import Product
# Create your views here.


def product_view(request):
    product = Product.object.all()

    return render(request, 'base.html', {'product': product})

