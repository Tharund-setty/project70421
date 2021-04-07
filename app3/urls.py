from django.urls import path
from app3 import views
app_name = 'app3'

urlpatterns = [
    path("<input>/",views.carry_input,name = "carryinput"),

]
    
