from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('',views.home,name='home'),
    path('enroll/',views.enroll,name='enroll'),
    path('signup/',views.signup,name='signup'),
    path('signup_patient/',views.signupPatient,name='signup_patient'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('dashboard/editProfile/',views.EditProfile, name='editProfile'),
    path('dashboard/signupOperator/',views.signupOperator, name='signupOperator'),
    path('dashboard/listOperator/deleteOperator/<id>/',views.deleteOperator, name='deleteOperator'),
    path('dashboard/listOperator/',views.listOperator, name='listOperator'),
    path('dashboard/createTrial/',views.createTrial, name='createTrial'),
    path('dashboard/listTrial/',views.listTrial, name='listTrial'),
    path('dashboard/listEnrollment/',views.listEnrollment, name='listEnrollment'),
    path('dashboard/listTrial/deleteTrial/<title>/',views.deleteTrial, name='deleteTrial'),
]

