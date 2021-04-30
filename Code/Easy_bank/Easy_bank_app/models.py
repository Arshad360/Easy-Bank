from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
    
class Loan(models.Model):
    types_of_loan = models.CharField(max_length=40, null=False)
    bank_name= models.CharField(max_length=70, null=False)
    interest_rate = models.CharField(max_length=30,null=False)
    processing_fee_range = models.CharField(max_length=40)
    loan_amount= models.CharField(max_length=50, null=False)
    tenure_range= models.CharField(max_length=70, null=False)
    
class Credit_card(models.Model):  
    bank_name = models.CharField(max_length=50)
    card_type= models.CharField(max_length=50)
    first_year_fee= models.CharField(max_length=50)
    rewards= models.CharField(max_length=50)
    joining_perks= models.CharField(max_length=50)

