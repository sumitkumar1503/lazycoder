from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail


def home_view(request):
    projects=models.Projects.objects.all()[0:6]

    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'coder/index.html',{'projects':projects})

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('customer-dashboard')
    else:
        return redirect('admin-dashboard')
def viewproject_view(request,longnameurl):
    project = models.Projects.objects.get(longnameurl=longnameurl)
    return render(request,'coder/viewproject.html',{'project':project})
def downloadproject_view(request,longnameurl):
    project = models.Projects.objects.get(longnameurl=longnameurl)
    return render(request,'coder/downloadproject.html',{'project':project})

def terms_view(request):
    return render(request,'coder/terms.html')
def privacy_view(request):
    return render(request,'coder/privacy.html')
def refund_view(request):
    return render(request,'coder/refund.html')
def aboutus_view(request):
    return render(request,'coder/aboutus.html')
def contactus_view(request):
    return render(request,'coder/contactus.html')
