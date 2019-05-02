from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def men(request):
    products_list_men = Product.objects.filter(category__name='men')
    return render(request, 'men.html', {"products_list_men": products_list_men})

def sports(request):
    products_list_sports = Product.objects.filter(category__name='sports')
    return render(request, 'sports.html', {"products_list_sports": products_list_sports})

def women(request):
    products_list_women = Product.objects.filter(category__name='women')
    return render(request, 'women.html', {"products_list_women": products_list_women})

@login_required(login_url='/users/register/')
def upvote(request, product_id):
    products = Product.objects.all()
    product = Product.objects.get(pk=product_id)
    product.upvotes += 1
    product.save()
    return redirect(request.META['HTTP_REFERER'])
    
@login_required(login_url='/users/register/')
def downvote(request, product_id):
    products = Product.objects.all()
    product = Product.objects.get(pk=product_id)
    product.upvotes -= 1
    product.save()
    return redirect(request.META['HTTP_REFERER'])