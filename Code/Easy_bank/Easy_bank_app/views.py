from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from . import models
from django.contrib import messages

# Create your views here.
def home_view(request):
  return render(request,'Easy_bank_app/homebase.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


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
            my_user_group = Group.objects.get_or_create(name='CUSTOMER')
            my_user_group[0].user_set.add(user)
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
    return render(request,'Easy_bank_app/compareandapply.html')

def contactus_sent_view(request):
    contactusForm=forms.ContactusForm()
    if request.method == 'POST':
        contactusForm = forms.ContactusForm(request.POST)
        if contactusForm.is_valid():
            contactusForm.save()
            return render(request, '')
    return render(request, 'Easy_bank_app/contact_us.html', {'contactusForm':contactusForm})

def contactus_sent_view_2(request):
    contactusForm=forms.ContactusForm()
    if request.method == 'POST':
        contactusForm = forms.ContactusForm(request.POST)
        if contactusForm.is_valid():
            contactusForm.save()
            return render(request, '')
    return render(request, 'Easy_bank_app/contact.html', {'contactusForm':contactusForm})

def contactus_view(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
            saverecord=models.Contactus()
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.phone=request.POST.get('phone')
            saverecord.message=request.POST.get('message')
            saverecord.save()
            messages.success(request,'Your message sent successfully. Thank you for contacting us!!!')
            return render(request,'Easy_bank_app/contact_us.html')
    else:
            return render(request,'Easy_bank_app/contact_us.html')
