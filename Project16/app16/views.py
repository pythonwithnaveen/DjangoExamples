from django.shortcuts import render,redirect
from app16.models import ProductModel

def openMainPage(request):
    if request.method == "POST":
        name = request.POST.get("product_name")
        price = request.POST.get("product_price")
        photo = request.FILES['product_photo']
        ProductModel(name=name,price=price,photo=photo).save()
        return redirect('main')

    else:
        return render(request,"index.html")


def viewall(request):
    products_list = ProductModel.objects.all()
    return render(request,"viewall.html",{"all_products":products_list})