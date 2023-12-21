from django.shortcuts import render,redirect, HttpResponse
from.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def Welcome(request):
    product = Product.objects.all()
    return render(request, "home.html", {"products":product})



def Add_product(request):
  
    if request.method == "GET":
        return render(request,"create_product.html")
    elif request.method == "POST":
        data = request.POST
        if not data.get("id"):
            try:
                Product.objects.create(Name = data.get("name"), MF_date = data.get("mf_date"),
                                    product_no = data.get("product number"))
            except Exception as msg:
                messages.error(request, f"Error: {msg}")
        else:
            product = Product.objects.get(id = data.get("id"))
            product.Name = data.get("name")
            product.MF_date = data.get("mf_date")
            product.product_no = data.get("product number")
            try:
                product.save()
            except Exception as msg:
                messages.error(request, f"Error: {msg}")
        return redirect("home")


def Update_product(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        return render(request, "create_product.html", {"all_products":product})



def Delete_product(request, id):
    try:
        products = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        products.is_deleted=True
        products.save()
        return redirect("home")
    

def Deleted_product(request):
    products = Product.objects.filter(is_deleted=True)
    return render(request, "deleted_product.html", {"all_products":products})


def Restore_product(request, id):
    try:
        products = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        products.is_deleted=False
        products.save()
        return redirect("deleted_product")
    

def permanantly_delete(request, id):
    try:
        Products = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        Products.delete()
        return redirect("home")
    