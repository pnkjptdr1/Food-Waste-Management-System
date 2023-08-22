from django.shortcuts import render,redirect
from DonateRecieve.models.product import Product
from DonateRecieve.models.category import Category
from DonateRecieve.models.donor import Donor
from django.views import View



class Donors(View):
   def post(self,request):
    product=request.POST.get('product')
    product=int(product)
    products=Product.get_product_by_id(product)
    return render(request,'donors.html',{'products':products})
 


 