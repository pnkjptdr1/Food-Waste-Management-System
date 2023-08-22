from django.contrib import admin
from django.urls import path
from DonateRecieve.views.old import *
from django.conf import settings
from django.conf.urls.static import static
from DonateRecieve.views import donors, signup,donor_login,index,addproduct,product,myproducts



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index.index, name='index'),

    path('products', product.Products.as_view(), name='product'),
    path('addproduct', addproduct.Addproduct.as_view(), name='addproduct'),
    path('donor_login',donor_login.Login.as_view(), name='donor_login'),
    path('logout/',donor_login.logout,name='logout'),
    path('signup',signup.Signup.as_view(),name='signup'),

    path('donor_contact',donors.Donors.as_view(),name='donor_contact'),
    path('myproducts', myproducts.Myproducts.as_view() ,name='myproducts'),


    path('admin_login', admin_login, name='admin_login'),
    path('dashboard', dashboard, name='dashboard'),
    path('addcategory', addcategory, name='addcategory'),
    path('managecategory', managecategory, name='managecategory'),
    path('editcategory<int:pid>', editcategory, name='editcategory'),
    path('deletecategory<int:pid>', deletecategory, name='deletecategory'),



    path('regdonors', regdonors, name='regdonors'),
    path('deletedonor<int:pid>', deletedonor, name='deletedonor'),
    path('listedproducts', listedproducts, name='listedproducts'),
    path('deleteproduct<int:pid>', deleteproduct, name='deleteproduct'),


   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
