from django.shortcuts import get_object_or_404, render
from .models import Category, Product
# Create your views here.
def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'store/product_list.html', {
        'categories': categories,
        'products': products,
        'category': None,
    })

def product_list_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category, available=True)
    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def product_detail(request, category_name, id):
    category = get_object_or_404(Category, name=category_name)
    product = get_object_or_404(Product, id=id, category=category, available=True)
    categories = Category.objects.all()
    return render(request, 'store/product_detail.html', {
        'product': product,
        'categories': categories
    })