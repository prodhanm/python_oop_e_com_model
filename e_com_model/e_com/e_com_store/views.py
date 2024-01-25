from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product

def home(request, category_slug=None):
    category_page = None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category_page, available=True)
        # The filter() function returns a query set of objects that match the
        # category based on their slug and are available.
    else:
        products = Product.objects.all().filter(available=True)
        # The all() function returns a query set of all objects in the database.
        # However, we added the filter() to return only all objects that are available.
    return render(request, 'home.html', {'category': category_page, 'products': products})

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("<h1>About page</h1>")

def product(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        # category__slug denotes in django, category.slug to access the slug field.
        # category__slug=category_slug, slug=product_slug denotes that we are looking
        # to access the category_slug (having the single underscore).
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})

