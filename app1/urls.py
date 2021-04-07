from django.urls import path
from app1 import views
app_name = 'app1'

urlpatterns = [
    
    path('sample1/',views.sample,name = 'sample1'),
    
]
