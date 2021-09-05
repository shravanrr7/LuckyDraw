from django.shortcuts import render,redirect

# Create your views here.
# from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            
            return redirect('login')

    context = {'form':form}
    return render(request, "register.html", context)

@unauthenticated_user
def loginpage(request):
    # if request.user.is_authenticated:
    #     return redirect('draw')
    # else:
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            if user.groups.filter(name='admin'):
                print("Its admin")
                return redirect('home')
            else:
                return redirect('draw')
            # login(request, user)

            # return redirect('draw')
        
        else:
            messages.info(request, 'Wrong account ')


    context = {}    
    return render(request, "login.html")


def logoutpage(request):
    logout(request)
    return redirect('login')
