from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.views.generic.base import RedirectView
urlpatterns = [
    path('',views.home,name='home'),

    path('enroll/<title>/',views.EnrollView.as_view(),name='enroll'),
    path('contact/<title>/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    #path('signup_patient/',views.signupPatient,name='signup_patient'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('login/',views.Login.as_view(), name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('dashboard/editProfile/',views.EditProfile, name='editProfile'),
    path('dashboard/signupOperator/',views.signupOperator, name='signupOperator'),
    path('dashboard/listOperator/deleteOperator/<id>/',views.deleteOperator, name='deleteOperator'),
    path('dashboard/listOperator/',views.listOperator, name='listOperator'),
    path('dashboard/createTrial/',views.createTrial, name='createTrial'),
    path('dashboard/listTrial/',views.listTrial, name='listTrial'),
    path('dashboard/listEnrollment/',views.listEnrollment, name='listEnrollment'),
    path('dashboard/listTrial/deleteTrial/<title>/',views.deleteTrial, name='deleteTrial'),


    # urls for testing purpose
    path('trial_detail/<str:title>/',views.DetailTrial.as_view(),name='trial_detail'),
    path('create_patient/', views.CreatePatient.as_view(), name='create_patient'),
    path('update_operator/<pk>/', views.UpdateOperator.as_view(), name='update_operator'),
    path('list_trial/', views.ListTrials.as_view(), name='list_trial'),
    # path('author/',views.Author.as_view(), name='author'),
    # path('go-to-django/', RedirectView.as_view(url='https://djangoproject.com'), name='go-to-django'),

]

