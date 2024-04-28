from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-author'),
    path('profile/',views.profile,name='profile')
]