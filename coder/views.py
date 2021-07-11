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
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'coder/index.html')

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('customer-dashboard')
    else:
        return redirect('admin-dashboard')