import http
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse
from DonateRecieve.models.donor import Donor
from django.contrib.auth.hashers import make_password
from django.views import View
from unicodedata import category
from DonateRecieve.models.category import Category


class Signup(View):
    def get(self,request):
       return render(request,'signup.html')
    
    def post(self,request):
       postData=request.POST
       name=postData.get('name')
      #  branch=postData.get('branch')
       address=postData.get('address')
      #  category=postData.get('category')
      #  room_no=postData.get('room_no')
       phone_no=postData.get('phone_no')
       email=postData.get('email')
       password=postData.get('password')
       password2=postData.get('pswd')
       if request.FILES:
            image=request.FILES['image']

       
       donor=Donor(name=name,address=address,
       phone_no=phone_no,email=email,password=password,image=image)
       
       error_message=self.validateDonor(donor)

       if(password != password2):
          error_message="Password does not matches!!"

       value={
             'name':name,
            #  'branch':branch,
             'address':address,
            #  'category':category,
            #  'room_no':room_no,
             'phone_no':phone_no,
             'email':email, 
             'image':image    
          }
 
      
       if not error_message:
           donor.password=make_password(donor.password)
           donor.register()
           return redirect('donor_login')
       else:
           data={
                  'error':error_message,
                  'values':value
              }
           return render(request,'signup.html',data)

            

    def validateDonor(self,donor):
        error_message=None
        if(not donor.name):
           error_message="Name Required !!"
        elif len(donor.name) < 4:
           error_message="Name is Too Short !!"
      #   elif(not donor.branch):
      #      error_message="Branch/Course Name Required !!"
        elif(not donor.address):
           error_message="address is Required !!"
        elif(not donor.phone_no):
           error_message="Phone No. Required !!"
        elif(len(donor.phone_no) != 10):
           error_message="Invalid Phone No !!"
        elif(not donor.email):
           error_message="Email Required !!"
        elif(not donor.password):
           error_message="Password Required !!"
        elif(len(donor.password)<6):
           error_message="Password Must be 6 char Long"
        elif(donor.isExists()):
           error_message="Email Already Registered ...!!"
        
        return error_message
