from django.urls import path,include
from .views import home

app_name = 'Home'

urlpatterns = [
    path('',home,name='home'),
    path('course/',include('courses.urls')),
]