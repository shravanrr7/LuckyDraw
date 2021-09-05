from django.urls import path
from .import views

urlpatterns=[
path('',views.index,name="homes"),
path('add',views.add,name="add"),
path('home',views.home,name="home"),

]