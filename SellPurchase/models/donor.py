from statistics import mode
from unicodedata import category
from django.db import models
from .category import Category


class Donor(models.Model):
    name=models.CharField(max_length=50)
    # branch=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    # category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    # room_no=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    image=models.ImageField(upload_to='uploads/products/',null=True,blank=True)
    
    def register(self):
        self.save()

    @staticmethod
    def get_student_by_email(email):
        try:
          return Donor.objects.get(email=email)
        except:
            return False
            
    
    def isExists(self):
        if Donor.objects.filter(email=self.email):
            return True
        
        return False