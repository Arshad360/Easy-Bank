
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group, User, auth
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

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
        return 
    else:
        return render(request, 'Easy_bank_app/admin_dashboard.html')

@login_required(login_url='adminlogin') 
def admin_dashboard_view(request):
    customercount=models.Customer.objects.all().count()
    
    easy_bank_app={
        'customercount':customercount,
        
    }
    return render(request,'Easy_Bank_app/admin_dashboard.html',context=easy_bank_app)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_home_view(request):
    return render(request,'Easy_bank_app/customer_home.html')
    
@login_required(login_url='adminlogin')
def view_customer_view(request):
    customers=models.Customer.objects.all()
    return render(request,'Easy_bank_app/view_customer.html',{'customers':customers})


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

def brac_bank_form_view(request):
    return render(request, 'Loan_form/carloan/brac.html')

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


