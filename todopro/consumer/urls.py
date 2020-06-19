from django.urls import path
from . import views


urlpatterns = [
path('profile',views.conprofile,name='profile'),
]
