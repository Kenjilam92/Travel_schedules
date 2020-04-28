from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('main',views.main),
    path('register',views.register),
    path('login',views.login)
    ]