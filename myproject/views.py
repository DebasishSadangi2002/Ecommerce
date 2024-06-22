from store.models import Category, Product 
from django.db.models import OuterRef, Subquery, Max
from django.shortcuts import render


def home(request):
    subquery = Product.objects.filter(
        category=OuterRef('pk'),
        available=True
    ).order_by('-updated').values('id')[:1]

    categories = Category.objects.annotate(
        latest_product_id=Subquery(subquery)
    )

    latest_products = Product.objects.filter(id__in=[category.latest_product_id for category in categories])

    return render(request, 'home.html', {
        'latest_products': latest_products,
    })