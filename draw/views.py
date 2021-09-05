from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import lotteadm
from numpy import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import nio
from datetime import date, datetime,time,timezone
import time

# Create your views here.
@login_required(login_url='login')
def draw(request):
        numbers = lotteadm.objects.all()
        print(numbers)
        key = [item.number for item in numbers]
        val = [item.price for item in numbers]
        # print(key,val)
        res = dict(zip(key, val))
        # print(res)
        kk=[]
        ii=len(res)-1
        # print(ii)
        prt=0.8/ii

        # print("values is" , prt)

        print(len(res))
        for i in res.values():
            if i == 'None':
                kk.append(prt)
            else:
                kk.append(.2)
        print(kk)
        x = random.choice(key, p=kk, size=(1))
        # print('keys are',key ,' and', kk)
        mm=str()
        for i in x:
            mm=mm+i
        # print(mm)

        return render(request,"draw.html",{'mm':mm})

@login_required(login_url='login')
def check(request):
    try:
        num=request.POST['number']
        if lotteadm.objects.filter(number=num).exists():
            prices=lotteadm.objects.filter(number=num)
            my_values = [item.price for item in prices]
            # print(my_values)
            mm=str()
            for i in my_values:
                mm=mm+i
            # print('the price is** ',mm)
            if mm == 'None':
                # print('none')
                messages.success(request, 'Better luck next time !!!! ')
                return render(request,"draw.html",{'price':prices})


            else:
                # auth data save
                # print('10000')
                vv=nio(amount=mm,dat=date.today(),tim=datetime.now().time(),user=request.user)
                vv.save()
                # end
                messages.success(request, 'Congragulations you won {mm}'.format(mm=mm))
                return render(request,"draw.html",{'price':prices})


            # return render(request,"draw.html",{'price':prices})
        else:  
            return render(request,"draw.html")
    except Exception as e:
        print(e)
        return render(request,"draw.html",{'price':"Error!!!"})

@login_required(login_url='login')
def show(request):
        log_user=request.user
        mem=nio.objects.filter(user=log_user)
        # print(mem)
        return render(request,'draw.html',{'mem':mem})



