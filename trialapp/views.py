from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect,HttpResponse
from .forms import InvestigatorForm
from .forms import InvestigatorSignupForm
from .models import Investigator, Trial
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from .models import Operator, Enrollment
from .forms import OperatorSignupForm 
from .forms import ListOperatorForm 
from .forms import EditOperatorForm, CreateTrialForm, PatientSignupForm, EnrollmentForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission, User



def home(request):
    #if not request.user.is_anonymous:
    #    trials = Trial.objects.filter(creator=request.user)
    #    operators = Operator.objects.filter(creator=request.user)
    #    print(trials)
    #    for o in operators:
    #        trials = trials | Trial.objects.filter(creator=o)

    #    print(trials)
        
    trials = Trial.objects.all()
    return render(request,'trialapp/home.html',{'trials':trials})
    



def signup(request):
    if request.method == 'POST':
        form = InvestigatorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return HttpResponseRedirect('/trialapp')
        else:
            print('not valid')
    else:
        form = InvestigatorSignupForm(request.POST)
                   
    return render(request,'trialapp/signup.html',{'form':form})




@login_required
def dashboard(request):
    
    #if request.method == 'POST':
        #return HttpResponseRedirect('createOperator')
    #else:
    return render(request,'trialapp/dashboard.html')




#@permission_required('trialApp.add_operator',raise_exception=True)
@login_required
def signupOperator(request):
    if request.method == 'POST':
        form = OperatorSignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponse('operator created')
        else:
            print('not valid')
    else:
        form = OperatorSignupForm(request.POST)

    return render(request,'trialapp/signup.html',{'form':form})



def signupPatient(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse('patient created')
        else:
            print('not valid')
    else:
        form = PatientSignupForm(request.POST)

    return render(request,'trialapp/signup.html',{'form':form})


@login_required
def createTrial(request):
    if request.method == 'POST':
        form = CreateTrialForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Trial Created successfully')

    else:
        form = CreateTrialForm()

    return render(request,'trialapp/createTrial.html',{'form':form})



@login_required
def listTrial(request):
    trials = Trial.objects.filter(creator=request.user)
    operators = Operator.objects.filter(creator=request.user)
    print(trials)
    for o in operators:
        trials = trials | Trial.objects.filter(creator=o)

    return render(request,'trialapp/listTrial.html',{'trials':trials})


@login_required
def listOperator(request):
    print(request.user.has_perm('trialapp.view_operator'))
    if request.method == 'POST':
        print(id)
        form = ListOperatorForm()
        

    #else:
        #form = DeleteOperatorForm(request.POST)
    operators = Operator.objects.filter(creator=request.user)
    
    return render(request,'trialapp/listOperator.html',{'operators':operators})



@login_required
def EditProfile(request):
    if request.method == 'POST':
        #op = Operator.objects.get(id=id)
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            
            #print(user.username)
            #inv = Investigator.objects.get(username=request.user)
            #inv.op = user
            #print(inv.op.password)
            return HttpResponse('operator updated')
        else:
            print(request.user)
            pass
    else:
        #op = Operator.objects.get(id=id)
        form = UserChangeForm(instance=request.user)
        print(request.user)
    return render(request,'trialapp/editprofile.html',{'form':form})



@login_required
def deleteOperator(request,id):
    op = Operator.objects.get(id=id)
    op.delete()
    return HttpResponse('Operator Deleted')

@login_required
def deleteTrial(request,title):
    tr = Trial.objects.get(title=title)
    tr.delete()
    return HttpResponse('Trial Deleted')



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/trialapp')



def enroll(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully Enrolled')
    
    form = EnrollmentForm()
    return render(request,'trialapp/enrollment.html',{'form':form})

def listEnrollment(request):
    enrolled = Enrollment.objects.all()
    return render(request,'trialapp/listEnrollment.html',{'enrolled':enrolled})
