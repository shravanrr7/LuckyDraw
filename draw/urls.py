from django.urls import path
from .import views

urlpatterns=[
path('draw',views.draw,name="draw"),
path('check',views.check,name="check"),
path('show',views.show,name="show")




]