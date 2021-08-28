
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Easy_bank_app import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='Easy_bank_app/adminlogin.html')),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('customerclick', views.customerclick_view),
    path('customersignup', views.customer_signup_view),  
    path('customerlogin', LoginView.as_view(template_name='Easy_bank_app/userlogin.html'),name='customerlogin'), 
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('customer-home', views.customer_home_view,name='customer-home'), 
    path('logout', LogoutView.as_view(template_name='Easy_bank_app/logout.html'), name='logout'),
    path('homebase', LoginView.as_view(template_name='Easy_bank_app/homebase.html'), name='homebase'),
    path('loan/', views.showdata),
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
    path('comparecreditcard/', views.credit_card_compare_view),
    path('compareloan/', views.compare_loan_view),
    path('Credit_card/', views.credit_card_view),
    path('Insertcareligibility/', views.Insertcareligibility),

    #### URL PATH STARTED FOR APPLICATION FORM OF CAR LOAN
    
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

    path('bracbankedu/', views.brac_bank_edu_form_view),
    path('citybankedu/', views.city_bank_edu_form_view),
    path('dhakabankedu/', views.dhaka_bank_edu_form_view),
    path('easternbankedu/', views.eastern_bank_edu_form_view),
    path('grameenbankedu/', views.grameen_bank_edu_form_view),
    path('habibbankedu/', views.habib_bank_edu_form_view),
    path('hsbcbankedu/', views.hsbc_bank_edu_form_view),
    path('jamunabankedu/', views.jamuna_bank_edu_form_view),
    path('janatabankedu/', views.janata_bank_edu_form_view),
    path('mitbbankedu/', views.mitb_bank_edu_form_view),
    path('onebankedu/', views.one_bank_edu_form_view),
    path('primebankedu/', views.prime_bank_edu_form_view),
    path('dutchbanglabankedu/', views.dbbl_bank_edu_form_view),
    path('standardbankedu/', views.standard_bank_edu_form_view),
    path('ucbbankedu/', views.ucb_bank_edu_form_view),
    path('uttarabankedu/', views.uttara_bank_edu_form_view),

    #### URL PATH ENDED FOR APPLICATION FORM OF EDUCATION LOAN

    #### URL PATH STARTED FOR APPLICATION FORM OF HOME LOAN

    
    path('citybankhome/', views.city_bank_home_form_view),
    path('dutchbanglabankhome/', views.dbbl_home_form_view),
    path('dhakabankhome/', views.dhaka_bank_home_form_view),
    path('easternbankhome/', views.eastern_bank_home_form_view),
    path('grameenbankhome/', views.grameen_bank_home_form_view),
    path('habibbankhome/', views.habib_bank_home_form_view),
    path('hsbcbankhome/', views.hsbc_bank_home_form_view),
    path('jamunabankhome/', views.jamuna_bank_home_form_view),
    path('janatabankhome/', views.janata_bank_home_form_view),
    path('mitbbankhome/', views.mitb_bank_home_form_view),
    path('onebankhome/', views.one_bank_home_form_view),
    path('primebankhome/', views.prime_bank_home_form_view),
    path('sonalibankhome/', views.sonali_bank_home_form_view),
    path('standardbankhome/', views.standard_bank_home_form_view),
    path('ucbbankhome/', views.ucb_bank_home_form_view),
    path('uttarabankhome/', views.uttara_bank_home_form_view),


    #### URL PATH ENDED FOR APPLICATION FORM OF HOME LOAN


    #### URL PATH STARTED FOR APPLICATION FORM OF LOAN AGAINST PROPERTY
    path('bracbanklap/', views.brac_bank_lap_form_view),
    path('citybanklap/', views.city_bank_lap_form_view),
    path('dutchbanglabanklap/', views.dbbl_lap_form_view),
    path('dhakabanklap/', views.dhaka_bank_lap_form_view),
    path('easternbanklap/', views.eastern_bank_lap_form_view),
    path('grameenbanklap/', views.grameen_bank_lap_form_view),
    path('habibbanklap/', views.habib_bank_lap_form_view),
    path('hsbcbanklap/', views.hsbc_bank_lap_form_view),
    path('jamunabanklap/', views.jamuna_bank_lap_form_view),
    path('janatabanklap/', views.janata_bank_lap_form_view),
    path('mitbbanklap/', views.mitb_bank_lap_form_view),
    path('onebanklap/', views.one_bank_lap_form_view),
    path('primebanklap/', views.prime_bank_lap_form_view),
    path('sonalibanklap/', views.sonali_bank_lap_form_view),
    path('standardbanklap/', views.standard_bank_lap_form_view),
    path('ucbbanklap/', views.ucb_bank_lap_form_view),
    path('uttarabanklap/', views.uttara_bank_lap_form_view),
    #### URL PATH ENDED FOR APPLICATION FORM OF LOAN AGAINST PROPERTY

    #### URL PATH STARTED FOR ELIGIBILITY CHECK FORM OF HOME LOAN

    path('homeloaneligibility/', views.homeloaneligibility_view ),
    path('carloaneligibility', views.carloaneligibility_view),
    path('educationloaneligibility/', views.educationloaneligibility_view ),
    path('personalloaneligibility/', views.personalloaneligibility_view),
    path('loanagainsteligibility/', views.loanagainstpropertyeligibility_view),

    path('showcontacts', views.show_contacts, name='showcontacts'),
    path('createpdf',views.pdf_report_create, name='createpdf'),
    #path('testhloan', views.testhloan_view, name='testhloan'),
    path('hform1', views.homeloan_one_view, name='hform1'),
    path('hform2', views.homeloan_two_view, name='hform2'),
    path('hform3', views.formthreedata, name='hform3'),
    path('hform4', views.homeloan_four_view, name='hform4'),
    path('hform5', views.homeloan_five_view, name='hform5'),
    path('brachf1', views.brac_home_loan_1, name='brachf1'),
    path('brachf2', views.brac_home_loan_2, name='brachf2'),
    path('brachf3', views.brac_home_loan_3, name='brachf3'),
    path('brachf4', views.brac_home_loan_4, name='brachf4'),
    path('brachf5', views.brac_home_loan_5, name='brachf5'),
  


    

]
