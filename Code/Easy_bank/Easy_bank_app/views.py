
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from . import forms, models
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group, User, auth
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from io import BytesIO
from django.template import Context, context

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.
def home_view(request):
  return render(request,'Easy_bank_app/homebase.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

def afterlogin_view(request): 
    if is_customer(request.user):
        return render(request, 'Easy_bank_app/customer_home.html')
    else:
        return render(request, 'Easy_bank_app/admin_dashboard.html')



@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    # for cards on dashboard
    customer= models.Customer.objects.all()
    customercount=models.Customer.objects.all().count()
    
    orders=models.Customer.objects.all()
    ordered_products=[]
    ordered_bys=[]
    for order in orders:
        ordered_product=models.Product.objects.all().filter(id=order.product.id)
        ordered_by=models.Customer.objects.all().filter(id = order.customer.id)
        ordered_products.append(ordered_product)
        ordered_bys.append(ordered_by)

    mydict={
    'customercount':customercount,
    'customer': customer,
    'data':zip(ordered_products,ordered_bys,orders),
    }
    return render(request,'Easy_Bank_app/admin_dashboard.html',context=mydict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_home_view(request):
    return render(request,'Easy_bank_app/customer_home.html')
    
@login_required(login_url='adminlogin')
def view_customer_view(request):
    customers=models.Customer.objects.all()

    cont={
    'customers': customers, 
    }
    return render(request,'Easy_bank_app/view_customer.html',{cont:customers})


def customerclick_view(request):
    
    return render(request, 'Easy_bank_app/userlogin.html')


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()     
    easy_bank_app={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    
    return render(request,'Easy_bank_app/usersignup.html',context=easy_bank_app)

        
def showdata(request): 
    results=models.Loan.objects.all()
    return render(request,'Easy_bank_app/loan.html',{"data": results})

def showdata_credit(request): 
    results=models.Credit_card.objects.all()
    return render(request,'Easy_bank_app/credit_card.html',{"data": results})


def slider_view(request):
    return render(request,'Easy_bank_app/slider.html')
 
def compare_view(request):
    return render(request,'Easy_bank_app/compare.html')

def compare_loan_view(request):
    return render(request, 'Easy_bank_app/allloan.html')

def credit_card_compare_view(request):
    return render(request, 'Easy_bank_app/compareandapply.html')

def contactus_view(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        
        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        }
        message = '''
        New message : {}
        
        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['email'], message, '', ['easybank444@gmail.com'])
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
            saverecord=models.Contactus()
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.phone=request.POST.get('phone')
            saverecord.message=request.POST.get('message')
            saverecord.save()
        
            return render(request,'Easy_bank_app/contact_us_sent.html')
    else:
            return render(request,'Easy_bank_app/contact_us.html')

def brac_view(request):     
    return render(request,'Easy_bank_app/brac.html')

def view_feedback_view(request):
    feedbacks=models.Contactus.objects.all().order_by('-id')
    return render(request,'Easy_bank_app/contact_us_view.html',{'feedbacks':feedbacks})

def car_loan_view(request):
    return render(request,'Easy_bank_app/carloan1.html')

def education_loan_view(request):   
    return render(request, 'Easy_bank_app/educationloan.html')

def home_loan_view(request):   
    return render(request, 'Easy_bank_app/Home_loan.html')

def emi_calculator_view(request):    
    return render(request, 'Easy_bank_app/emi_calculator.html')

def personal_loan_view(request):   
    return render(request, 'Easy_bank_app/personal.html')

def startup_loan_view(request):   
    return render(request, 'Easy_bank_app/Startup.html')

def loan_ag_pro_view(request):   
    return render(request, 'Easy_bank_app/Loanagainstproperty.html')

def loan_calculator_view(request):   
    return render(request, 'Easy_bank_app/loancalculator.html')

#### VIEWS STARTED FOR APPLICATION FORM OF CAR LOAN

def city_bank_form_view(request):
    return render(request, 'Loan_form/carloan/city.html')

def dhaka_bank_form_view(request):
    return render(request, 'Loan_form/carloan/dhkbank.html')

def eastern_bank_form_view(request):
    return render(request, 'Loan_form/carloan/easternbank.html')

def grameen_bank_form_view(request):
    return render(request, 'Loan_form/carloan/grameenbank.html')

def habib_bank_form_view(request):
    return render(request, 'Loan_form/carloan/habibbank.html')

def hsbc_bank_form_view(request):
    return render(request, 'Loan_form/carloan/hsbcbank.html')

def jamuna_bank_form_view(request):
    return render(request, 'Loan_form/carloan/jamuna.html')

def janata_bank_form_view(request):
    return render(request, 'Loan_form/carloan/janata.html')

def mitb_bank_form_view(request):
    return render(request, 'Loan_form/carloan/mitb.html')

def one_bank_form_view(request):
    return render(request, 'Loan_form/carloan/one.html')

def prime_bank_form_view(request):
    return render(request, 'Loan_form/carloan/prime.html')

def sonali_bank_form_view(request):
    return render(request, 'Loan_form/carloan/sonali.html')

def standard_bank_form_view(request):
    return render(request, 'Loan_form/carloan/standard.html')

def ucb_bank_form_view(request):
    return render(request, 'Loan_form/carloan/ucb.html')

def uttara_bank_form_view(request):
    return render(request, 'Loan_form/carloan/uttara.html')

#### VIEWS ENDED FOR APPLICATION FORM OF CAR LOAN

#### VIEWS STARTED FOR APPLICATION FORM OF EDUCATION LOAN
def brac_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/brac.html')

def city_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/city.html')

def dhaka_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/dhkbank.html')

def eastern_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/eastern.html')

def grameen_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/grameenbank.html')

def habib_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/habib.html')

def hsbc_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/hsbc.html')

def jamuna_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/jamuna.html')

def janata_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/janata.html')

def mitb_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/mitb.html')

def one_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/one.html')

def prime_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/prime.html')

def dbbl_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/dbbl.html')

def standard_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/standard.html')

def ucb_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/ucb.html')

def uttara_bank_edu_form_view(request):
    return render(request, 'Loan_form/educationloan/uttara.html')
  
#### VIEWS ENDED FOR APPLICATION FORM OF EDUCATION LOAN

#### VIEWS STARTED FOR APPLICATION FORM OF HOME LOAN

def brac_bank_home_form_view(request):
     return render(request, 'Loan_form/homeloan/brac.html')

def city_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/city.html')

def dbbl_home_form_view(request):
    return render(request, 'Loan_form/homeloan/dbbl.html')

def dhaka_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/dhkbank.html')

def eastern_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/eastern.html')

def grameen_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/grameenbank.html')

def habib_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/habib.html')

def hsbc_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/hsbc.html')

def jamuna_bank_home_form_view(request):
    return render(request, 'Loan_formhomeloan/jamuna.html')

def janata_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/janata.html')

def mitb_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/mitb.html')

def one_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/one.html')

def prime_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/prime.html')

def sonali_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/sonali.html')

def standard_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/standard.html')

def ucb_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/ucb.html')

def uttara_bank_home_form_view(request):
    return render(request, 'Loan_form/homeloan/uttara.html')

#### VIEWS ENDED FOR APPLICATION FORM OF HOME LOAN

#### VIEWS STARTED FOR APPLICATION FORM OF LOAN AGAINST PROPERTY

def brac_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/brac.html')

def city_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/city.html')

def dbbl_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/dbbl.html')

def dhaka_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/dhkbank.html')

def eastern_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/eastern.html')

def grameen_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/grameenbank.html')

def habib_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/habib.html')

def hsbc_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/hsbc.html')

def jamuna_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/jamuna.html')

def janata_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/janata.html')

def mitb_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/mitb.html')

def one_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/one.html')

def prime_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/prime.html')

def sonali_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/sonali.html')

def standard_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/standard.html')

def ucb_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/ucb.html')

def uttara_bank_lap_form_view(request):
    return render(request, 'Loan_form/loanagainstproperty/uttara.html')

#### VIEWS ENDED FOR APPLICATION FORM OF LOAN AGAIST PROPERTY

def homeloaneligibility_view(request):
    return render(request, 'Eligibility_Form/homeloan.html')

def carloaneligibility_view(request):
    return render(request, 'Eligibility_Form/carloan.html')

def educationloaneligibility_view(request):
    return render(request, 'Eligibility_Form/educationloan.html')

def personalloaneligibility_view(request):
    return render(request, 'Eligibility_Form/personalloan.html')

def loanagainstpropertyeligibility_view(request):
     return render(request, 'Eligibility_Form/loanagainst.html')

def credit_card_view(request):
    return render(request,'Easy_bank_app/credit_card.html')

def Insertcareligibility(request):
    if request.method=='POST':
        
        bangladeshi = request.POST.get('bangladeshi')
        username = request.POST.get('username')
        age = request.POST.get('age')
        number = request.POST.get('number')
        gender = request.POST.get('gender')
        net_income = request.POST.get('net_income')
        email = request.POST.get('email')

        data = {
            'bangladeshi':  bangladeshi,
            'username': username,
            'age': age,
            'number':number,
            'gender':gender,
            'net_income':net_income,
            'email':email
        }

        if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
            saverecord=models.Carloaneligibility()
            saverecord.bangladeshi=request.POST.get('bangladeshi')
            saverecord.username=request.POST.get('username')
            saverecord.age=request.POST.get('age')
            saverecord.number=request.POST.get('number')
            saverecord.gender=request.POST.get('gender')
            saverecord.net_income=request.POST.get('net_income')
            saverecord.email=request.POST.get('email')
            saverecord.save()

       # if request.POST.get('bangladeshi') and request.POST.get('username') and request.POST.get('age') and request.POST.get('number') and request.POST.get('gender') and request.POST.get('net_income') and request.POST.get('email'):
        #    saverecord=models.Carloaneligibility()
        #    saverecord.bangladeshi=request.POST.get('bangladeshi')
         #   saverecord.username=request.POST.get('username')
         #   saverecord.age=request.POST.get('age')
         #   saverecord.number=request.POST.get('number')
         #   saverecord.gender=request.POST.get('gender')
         #  saverecord.net_income=request.POST.get('net_income')
         #   saverecord.email=request.POST.get('email')
         #   saverecord.save()
        # return HttpResponse('brac')
           
    # else:
        return render(request,'Eligibility_Form/carloan.html')

def homeloan_one_view(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.hloanform()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('hform2')
            
    else:
         return render(request, 'Separate_Form/hform1.html')
    
def homeloan_two_view(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.hloanform2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('hform3')
    
    else:
         return render(request, 'Separate_Form/hform2.html')
            
def formthreedata(request):
    if request.method=='POST':
        if request.POST.get('property_type') and request.POST.get('floor_size') and request.POST.get('flat_no') and request.POST.get('nationality_2') and request.POST.get('utility') and request.POST.get('expected_possesion') and request.POST.get('date_expected'):
            save=models.hloanform3()
            save.property_type =request.POST.get('property_type')
            save.floor_size =request.POST.get('floor_size')
            save.flat_no =request.POST.get('flat_no')
            save.nationality_2=request.POST.get('nationality_2')
            save.utility =request.POST.get('utility')
            save.expected_possesion =request.POST.get('expected_possesion')
            save.date_expected =request.POST.get('date_expected')
            save.save()
            return HttpResponseRedirect('hform4')

    else:
        return render(request,'Separate_Form/hform3.html')
   
def homeloan_four_view(request):
    if request.method=='POST':
        if request.POST.get('home_area') and request.POST.get('loan_requested') and request.POST.get('balance_amount') and request.POST.get('payment_source') and request.POST.get('property_selected') and request.POST.get('contact_2') and request.POST.get('email_3'):

            saverecord=models.hloanform4()
            saverecord.home_area=request.POST.get('home_area')
            saverecord.loan_requested=request.POST.get('loan_requested')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.payment_source=request.POST.get('payment_source')
            saverecord.property_selected=request.POST.get('property_selected')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('hform5')
            
    else:
         return render(request, 'Separate_Form/hform4.html')

def homeloan_five_view(request):
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.hloanform5()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('hform1')
            
    else:
         return render(request, 'Separate_Form/hform5.html')

def brac_home_loan_1(request):
    if request.method=='POST':
        if request.POST.get('applicants_name') and request.POST.get('applicants_full_name') and request.POST.get('applicants_father_name') and request.POST.get('applicants_mother_name') and request.POST.get('nationality') and request.POST.get('gender') and request.POST.get('contatct_no') and request.POST.get('email') and request.POST.get('nid') and request.POST.get('loan_type') :

            saverecord=models.brac_home_loan_form1()
            saverecord.applicants_name=request.POST.get('applicants_name')
            saverecord.applicants_full_name=request.POST.get('applicants_full_name')
            saverecord.applicants_father_name=request.POST.get('applicants_father_name')
            saverecord.applicants_mother_name=request.POST.get('applicants_mother_name')
            saverecord.nationality=request.POST.get('nationality')
            saverecord.gender=request.POST.get('gender')
            saverecord.contatct_no=request.POST.get('contatct_no')
            saverecord.email=request.POST.get('email')
            saverecord.nid=request.POST.get('nid')
            saverecord.loan_type=request.POST.get('loan_type')
            saverecord.save()
            return HttpResponseRedirect('brachf2')
            
    else:
         return render(request, 'brac_bank_home_loan/h1.html')

def brac_home_loan_2(request):
    if request.method=='POST':
        if request.POST.get('full_address') and request.POST.get('city') and request.POST.get('postal_code') and request.POST.get('p_address') and request.POST.get('second_contact_no') and request.POST.get('second_email') :

            saverecord=models.brac_home_loan_form2()
            saverecord.full_address=request.POST.get('full_address')
            saverecord.city=request.POST.get('city')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.second_contact_no=request.POST.get('second_contact_no')
            saverecord.second_email=request.POST.get('second_email')
            saverecord.save()
            return HttpResponseRedirect('brachf3')
    
    else:
         return render(request, 'brac_bank_home_loan/h2.html')
    
def brac_home_loan_3(request):
    if request.method=='POST':
        if request.POST.get('property_type') and request.POST.get('floor_size') and request.POST.get('flat_no') and request.POST.get('nationality_2') and request.POST.get('utility') and request.POST.get('expected_possesion') and request.POST.get('date_expected'):
            save=models.brac_home_loan_form3()
            save.property_type =request.POST.get('property_type')
            save.floor_size =request.POST.get('floor_size')
            save.flat_no =request.POST.get('flat_no')
            save.nationality_2=request.POST.get('nationality_2')
            save.utility =request.POST.get('utility')
            save.expected_possesion =request.POST.get('expected_possesion')
            save.date_expected =request.POST.get('date_expected')
            save.save()
            return HttpResponseRedirect('brachf4')

    else:
        return render(request,'brac_bank_home_loan/h3.html')

def brac_home_loan_4(request):
    if request.method=='POST':
        if request.POST.get('home_area') and request.POST.get('loan_requested') and request.POST.get('balance_amount') and request.POST.get('payment_source') and request.POST.get('property_selected') and request.POST.get('contact_2') and request.POST.get('email_3'):

            saverecord=models.brac_home_loan_form4()
            saverecord.home_area=request.POST.get('home_area')
            saverecord.loan_requested=request.POST.get('loan_requested')
            saverecord.balance_amount=request.POST.get('balance_amount')
            saverecord.payment_source=request.POST.get('payment_source')
            saverecord.property_selected=request.POST.get('property_selected')
            saverecord.contact_2=request.POST.get('contact_2')
            saverecord.email_3=request.POST.get('email_3')
            saverecord.save()
            return HttpResponseRedirect('brachf5')
            
    else:
         return render(request, 'brac_bank_home_loan/h4.html')

def brac_home_loan_5(request):
    if request.method=='POST':
        if request.POST.get('organisation_name') and request.POST.get('designation_department') and request.POST.get('office_address') and request.POST.get('allowness') and request.POST.get('additional_income') and request.POST.get('salary_total') and request.POST.get('office_no') :

            saverecord=models.brac_home_loan_form5()
            saverecord.organisation_name=request.POST.get('organisation_name')
            saverecord.designation_department=request.POST.get('designation_department')
            saverecord.office_address=request.POST.get('office_address')
            saverecord.allowness=request.POST.get('allowness')
            saverecord.additional_income=request.POST.get('additional_income')
            saverecord.salary_total=request.POST.get('salary_total')
            saverecord.office_no=request.POST.get('office_no')
            saverecord.save()
            return HttpResponseRedirect('brachf1')
            
    else:
         return render(request, 'brac_bank_home_loan/h5.html')      

def homeloanform1(request):
    return render(request, 'Separate_Form/hform1.html')

def homeloanform2(request):
    return render(request, 'Separate_Form/hform2.html')

def homeloanform3(request):
    return render(request, 'Separate_Form/hform3.html')

def homeloanform4(request):
    return render(request, 'Separate_Form/hform4.html')

def homeloanform5(request):
    return render(request, 'Separate_Form/hform5.html')

def show_contacts(request):
    contacts=models.Contactus.objects.all()

    context= {
        'contacts':contacts
    }

    return render(request, 'Easy_bank_app/showinfo.html', context)



def show_brac_home_loan_form(request):
    brac_home_loan1=models.brac_home_loan_form1.objects.all()
    brac_home_loan2=models.brac_home_loan_form2.objects.all()
    brac_home_loan3=models.brac_home_loan_form3.objects.all()
    brac_home_loan4=models.brac_home_loan_form4.objects.all()
    brac_home_loan5=models.brac_home_loan_form5.objects.all()

    context= {
        'brac_home_loan1':brac_home_loan1,
        'brac_home_loan2':brac_home_loan2,
        'brac_home_loan3':brac_home_loan3,
        'brac_home_loan4':brac_home_loan4,
        'brac_home_loan5':brac_home_loan5
    }

    return render(request, 'All_home_loan/brac_bank_home.html', context)



def pdf_report_create2(request):
    brac_home_loan1=models.brac_home_loan_form1.objects.all()
    brac_home_loan2=models.brac_home_loan_form2.objects.all()
    brac_home_loan3=models.brac_home_loan_form3.objects.all()
    brac_home_loan4=models.brac_home_loan_form4.objects.all()
    brac_home_loan5=models.brac_home_loan_form5.objects.all()
  

    template_path = 'All_home_loan/brac_bank_home_loan_pdf.html'

    context= {
        'brac_home_loan1':brac_home_loan1,
        'brac_home_loan2':brac_home_loan2,
        'brac_home_loan3':brac_home_loan3,
        'brac_home_loan4':brac_home_loan4,
        'brac_home_loan5':brac_home_loan5
    
    }
    

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="home_loan_application.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def pdf_report_create(request):
    contacts=models.Contactus.objects.all()

    template_path = 'Easy_bank_app/contactpdf.html'

    context = {'contacts': contacts}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contactus_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
   # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def brac_edu_loan_view(request):
    return render(request, 'brac_edu_loan/h1.html')

def brac_edu_loan_view2(request):
    return render(request, 'Separate_Form/h1.html')

