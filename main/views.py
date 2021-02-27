from django.shortcuts import render
from products.models import Product


def main_page(request):
    products = None
    if request.method == "POST":
        name = request.POST["name"]
        products = Product.objects.filter(name__contains=name)
    else:
        products = Product.objects.all()
    d = {
        "products": products,
    }
    return render(request, "main/index.html", context=d)
