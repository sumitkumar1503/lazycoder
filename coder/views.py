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
import razorpay

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
    template_name='projects/'+project.htmlpage
    return render(request,template_name,{'project':project})

def downloadproject_view(request,longnameurl):
    project = models.Projects.objects.get(longnameurl=longnameurl)
    if project.price == 0:
        return render(request,'coder/downloadproject.html',{'project':project})
    else:
        amount=project.price*100
        if request.method=='POST':
            project = models.Projects.objects.get(longnameurl=longnameurl)
            client = razorpay.Client(auth=("rzp_live_8iylMiR7jz4h5S", "22ZmxzzsF8GXMelRA85Rs4bm"))
            order_amount = project.price*100
            order_currency = 'INR'
            xyz = client.order.create(dict(amount=order_amount, currency='INR', payment_capture='1'))
            if xyz['status'] == 'captured':
                return render(request,'coder/payment-success.html',{'project':project})
            else:
                return render(request,'coder/payment.html',{'project':project,'amount':amount})
        return render(request,'coder/payment.html',{'project':project,'amount':amount})



'''
def downloadproject_view(request,longnameurl):
    project = models.Projects.objects.get(longnameurl=longnameurl)
    return render(request,'coder/downloadproject.html',{'project':project})
'''


def showallproject_view(request):
    projects=models.Projects.objects.all()
    return render(request,'coder/all-projects-by-lazycoder.html',{'projects':projects})

def showpaidproject_view(request):
    projects=models.Projects.objects.all().exclude(price = 0)
    return render(request,'coder/paid-projects-by-lazycoder.html',{'projects':projects})


def showfreeproject_view(request):
    projects=models.Projects.objects.all().filter(price=0)
    return render(request,'coder/free-projects-by-lazycoder.html',{'projects':projects})

def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    projects=models.Projects.objects.all().filter(name__icontains=query)
    return render(request,'coder/search-result.html',{'projects':projects})

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
