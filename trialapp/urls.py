from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    '''path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),

    path('dashboard/',views.dashboard, name='dashboard'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('dashboard/editProfile/',views.EditProfile, name='editProfile'),
    path('dashboard/signupOperator/',views.signupOperator, name='signupOperator'),
    path('dashboard/listOperator/deleteOperator/<id>/',views.deleteOperator, name='deleteOperator'),
    #path('dashboard/listOperator/updateOperator/<id>/',views.updateOperator, name='updateOperator'),
    path('dashboard/listOperator/',views.listOperator, name='listOperator'),'''
]

