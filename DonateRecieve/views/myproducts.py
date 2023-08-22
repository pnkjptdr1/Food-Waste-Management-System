from email.mime import image
from itertools import product
from django.shortcuts import render , redirect
from DonateRecieve.models.donor import Donor
from DonateRecieve.models.category import Category
from django.views import  View
from DonateRecieve.models.product import  Product
from django.core.files.storage import FileSystemStorage
 
 

class Myproducts(View):
    def get(self ,request):
        donor=request.session.get('donor')
        products = Product.get_products_by_donor(donor)
        return render(request , 'myproducts.html' , {'products' : products} )


    def post(self ,request):
          product_id=request.POST.get('product')
          Product.delete_product_by_id(product_id)
          donor=request.session.get('donor')
          products = Product.get_products_by_donor(donor)
          return render(request , 'myproducts.html' , {'products' : products} )

           
         
   

     