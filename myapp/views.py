from django.http.response import HttpResponse
from django.shortcuts import render
from .models import lotteadm
from accounts.decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.http import HttpRequest
# def home(request):
# 	return render(request,"index.html")

@unauthenticated_user
def index(request):
	return render(request,"home.html")

@login_required(login_url='login')
@admin_only
def home(request):
    return render(request,"index.html")


@login_required(login_url='login')
@admin_only
def add(request):
    try:
        number=request.POST['number']
        price=request.POST['price']
        # nn=lotteadm.objects.values_list('number', flat=True) 
        # print(nn)   
        if lotteadm.objects.filter(number=number).exists():
            return render(request,"index.html",{'responseDic':"alredy exists please enter a new value"})
        else:
            lotte=lotteadm(number=number,price=price)
            lotte.save()
            return render(request,"index.html",{'responseDic':"Data added"})
    except Exception as e:
        print(e)
        return render(request,"index.html",{'responseDic':"Data not added"})






