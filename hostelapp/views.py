
from audioop import reverse
from unicodedata import name
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from .models import Admin_Outpass_Details, Outpass_Details,Complaint_Details, Student_Details
from django.views.decorators.csrf import csrf_exempt
from .forms import Admin_Complaint_detail_form, Admin_Outpass_detail_form, Outpass_detail_form,Complaint_detail_form
from .models import Outpass_Details
from django.contrib import messages
def home(request):
    return render(request,"Home.html")
def index(request):
    return render(request,'index.html')
def outpasslist (request):
    admin_outpass_list=Outpass_Details.objects.all()
    return render(request,'Outpass-List.html',{'admin_outpass_list':admin_outpass_list})
def reportlist (request):
    report_list=Complaint_Details.objects.all()
    return render(request,'Report-List.html',{'report_list':report_list})
def reportform(request,oid):
    object = Complaint_Details.objects.filter(id=oid).first()
    return render(request, "Report-Form.html", {'object':object})
def adminoutpassform(request,oid):
    object = Admin_Outpass_Details.objects.filter(id=oid).first()
    return render(request, "Admin_Approve_Outpass.html", {'object':object})
def approvaloutpassform(request,oid):
    object = Outpass_Details.objects.filter(id=oid).first()
    return render(request, "Outpass-Form.html", {'object':object})
def outpassapproval (request,regno):
    stu=Student_Details.objects.filter(regno=regno).first()
    outpass_list=Outpass_Details.objects.filter(regno=regno) 

    context={'outpass_list':outpass_list,'stu':stu}
    return render(request,'Outpass-Approval.html',context)
def outpass (request,regno):
    stu=Student_Details.objects.filter(regno=regno).first()
    return render(request,'Outpass.html',{'stu':stu})

def report(request,regno):
    stu=Student_Details.objects.filter(regno=regno).first()
    return render(request,'Report.html',{'stu':stu})

@csrf_exempt
def outpassupload(request):
    if (request.method=='POST'):
        print(request.POST)
        form=Outpass_detail_form(request.POST,request.FILES)
        admin_form=Admin_Outpass_detail_form(request.POST,request.FILES)   
        form.save()         
        admin_form.save()        
    return render(request,'Outpass-Form.html')

def outpassdetailsget(request):
    outpass_list=Outpass_Details.objects.all()
    
    return render(request,'Outpass-List.html',{'outpass_list':outpass_list})

@csrf_exempt
def complaintupload(request):
    if (request.method=='POST'):
        form=Complaint_detail_form(request.POST,request.FILES)
        admin_form=Admin_Complaint_detail_form(request.POST,request.FILES)
        form.save() 
        admin_form.save() 
    return render(request,'Outpass-Form.html')

@csrf_exempt
def statusupload(request,aid):
    if (request.method=='POST'):
        object = Admin_Outpass_Details.objects.filter(id=aid).first()
        upobj=Outpass_Details.objects.get(id=object.id)
        if(request.POST['submitclicked']=="Decline"):
            upobj.status="Decline"
        elif(request.POST['submitclicked']=="Approve"):
            upobj.status="Approve"
        upobj.save() 
    return render(request,"Outpass-List.html")

@csrf_exempt
def login(request):
    if (request.method=='POST'):
 
        
        stu_check=Student_Details.objects.filter(email=request.POST['email'])
        if(stu_check):
            stu=Student_Details.objects.get(email=request.POST['email'])
            if(request.POST['password']==stu.password):
                if(request.POST['email']=="admin@ssn.edu.in"):
                    admin_outpass_list=Outpass_Details.objects.all()
                    return render(request,'Outpass-List.html',{'admin_outpass_list':admin_outpass_list})
                    
                else:
                    return render(request,'Outpass.html',{'stu':stu})
            else:
                messages.error(request,'Login Failed !!')
                return redirect('home')
        else:
            messages.error(request,'Login Failed !!')
            return redirect('home')
