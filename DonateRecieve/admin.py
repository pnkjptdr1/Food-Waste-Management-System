from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.donor import Donor


# Register your models here.

admin.site.register(Product)
admin.site.register(Donor)
admin.site.register(Category)


 

