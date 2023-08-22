

from django.shortcuts import render,redirect,HttpResponseRedirect
from DonateRecieve.models.product import Product
from DonateRecieve.models.category import Category
from DonateRecieve.models.donor import Donor
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    return_url=None
    def get(self,request):
        Login.return_url=request.GET.get('return_url')
        return render(request,'donor_login.html')

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        donor=Donor.get_donor_by_email(email)
        error_message = None
        if donor:
            flag = check_password(password,donor.password)
            if flag:
                request.session['donor']=donor.id
                
                if Login.return_url:
                   return HttpResponseRedirect(Login.return_url)
                else:
                   Login.return_url=None
                   return redirect('index')
            else:
                error_message = 'Email or Password Invalid ...!!'
        else:
            error_message = 'Email or Password Invalid ...!!'
        return render(request,'donor_login.html',{'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('index')





 