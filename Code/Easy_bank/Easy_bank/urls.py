"""Easy_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Easy_bank_app import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
     path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='Easy_bank_app/adminlogin.html')),
     path('customerclick', views.customerclick_view),
    path('customersignup', views.customer_signup_view),  
    path('customerlogin', LoginView.as_view(template_name='Easy_bank_app/userlogin.html'),name='customerlogin'), 
    path('loan/', views.showdata),
    path('credit_card/', views.showdata_credit),
    path('slider/', views.slider_view),
    path('compareandapply/',views.compare_view),
    path('contactus/',views.contactus_view),
    path('brac/',views.brac_view),
    path('contactusview/', views.view_feedback_view),
    path('carloan/', views.car_loan_view),
    path('educationloan/', views.education_loan_view),
    path('homeloan/', views.home_loan_view),
    path('startuploan/', views.startup_loan_view),
    path('loanagainstproperty/', views.loan_ag_pro_view),
    path('personalloan/', views.personal_loan_view), 

    path('emicalculator/', views.emi_calculator_view),
    path('loancalculator/', views.loan_calculator_view),


    #### URL PATH STARTED FOR APPLICATION FORM OF CAR LOAN
    path('bracbank/', views.brac_bank_form_view),
    path('citybank/', views.city_bank_form_view),
    path('dhakabank/', views.dhaka_bank_form_view),
    path('easternbank/', views.eastern_bank_form_view),
    path('grameenbank/', views.grameen_bank_form_view),
    path('habibbank/', views.habib_bank_form_view),
    path('hsbcbank/', views.hsbc_bank_form_view),
    path('jamunabank/', views.jamuna_bank_form_view),
    path('janatabank/', views.janata_bank_form_view),
    path('mitbbank/', views.mitb_bank_form_view),
    path('onebank/', views.one_bank_form_view),
    path('primebank/', views.prime_bank_form_view),
    path('sonalibank/', views.sonali_bank_form_view),
    path('standardbank/', views.standard_bank_form_view),
    path('ucbbank/', views.ucb_bank_form_view),
    path('uttarabank/', views.uttara_bank_form_view),

    #### URL PATH ENDED FOR APPLICATION FORM OF CAR LOAN
  

    #### URL PATH STARTED FOR APPLICATION FORM OF EDUCATION LOAN

    path('bracbank/', views.brac_bank_edu_form_view),
    path('citybank/', views.city_bank_edu_form_view),
    path('dhakabank/', views.dhaka_bank_edu_form_view),
    path('easternbank/', views.eastern_bank_edu_form_view),
    path('grameenbank/', views.grameen_bank_edu_form_view),
    path('habibbank/', views.habib_bank_edu_form_view),
    path('hsbcbank/', views.hsbc_bank_edu_form_view),
    path('jamunabank/', views.jamuna_bank_edu_form_view),
    path('janatabank/', views.janata_bank_edu_form_view),
    path('mitbbank/', views.mitb_bank_edu_form_view),
    path('onebank/', views.one_bank_edu_form_view),
    path('primebank/', views.prime_bank_edu_form_view),
    path('dutchbanglabank/', views.dbbl_bank_edu_form_view),
    path('standardbank/', views.standard_bank_edu_form_view),
    path('ucbbank/', views.ucb_bank_edu_form_view),
    path('uttarabank/', views.uttara_bank_edu_form_view)

    #### URL PATH ENDED FOR APPLICATION FORM OF EDUCATION LOAN
]
