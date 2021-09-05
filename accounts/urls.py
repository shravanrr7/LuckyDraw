from django.urls import path
from .import views

urlpatterns=[
path('register',views.register,name="register"),
path('loginpage',views.loginpage,name="login"),
path('logout',views.logoutpage,name="logout"),

]