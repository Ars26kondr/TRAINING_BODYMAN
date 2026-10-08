from django.shortcuts import render
from .models import Slide
from .models import Products
import httpx

def main_page(r):
    slides=Slide.objects.all()
    products=Products.objects.all()
    return render(r, 'main_page.html', {'slides': slides, 'products': products})

def search_results(r):
    product_info=r.GET.get("A")
    results=[]
    if product_info:
        results=Products.objects.filter(Name__icontains=product_info)
    return render(r, 'results.html', {'product_result': results})

def profile(r):
    return render(r, 'profile.html' )
    
def shop(r):
    return render(r, 'shop.html' )

def chat(r):
    return render(r, 'chat.html')