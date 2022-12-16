from django.contrib import admin
from django.urls import path,include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('login/',views.login,name="login"),
    path('login/outpass/<str:regno>', views.outpass, name='outpass'),
    path('outpassapproval/<str:regno>', views.outpassapproval, name='outpassapproval'),
    path('login/report/<str:regno>', views.report, name='report'),
    path('login/outpasslist/', views.outpasslist, name='outpasslist'),
    path('reportlist/', views.reportlist, name='reportlist'),
    path('submit/outpassform',views.outpassdetailsget,name='outpassdetails'),
    path('outpass/submit',views.outpassupload,name='outpasscreate'),
    path('report/submit',views.complaintupload,name='complaintcreate'),
    path('reportform/<int:oid>/', views.reportform, name='reportforid'),
    path('approvaloutpassform/<int:oid>/', views.approvaloutpassform, name='approvaloutpassforid'),
    path('adminoutpassform/<int:oid>/', views.adminoutpassform, name='adminoutpassforid'),
    path('adminopapproval/<int:aid>/', views.statusupload, name='adminopapproval')
        
]
