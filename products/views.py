from products.forms import ProductForm
from products.models import Product
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
class CreateProductView(CreateView):
    redirect_field_name = 'products/product_form.html'
    form_class = ProductForm
    model = Product