from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect,HttpResponse
from .forms import InvestigatorSignupForm
from .models import Investigator, Trial
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from .models import Operator, Enrollment
from .forms import OperatorSignupForm, ContactForm
from .forms import ListOperatorForm 
from .forms import CreateTrialForm, PatientSignupForm
from django.views import View


def home(request):
        
    trials = Trial.objects.all()
    return render(request,'trialapp/dashboardnew.html',{'trials':trials})
    



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
                   
    return render(request,'trialapp/userSignup.html',{'form':form})




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

    return render(request,'trialapp/userSignup.html',{'form':form, 'successful_submit': True})



class EnrollView(View):
    form_class = PatientSignupForm
    template_name='trialapp/userSignup.html'

    def get_queryset(self):
        return self.kargs['title']

    def get(self, request,*args, **kargs):
        print(self.args['title'])
        form = self.form_class()
        print('get request')
        print(self.get_queryset())
        return render(request, self.template_name, {'form': form})



    def post(self, request, *args, **kargs):
        form = self.form_class(request.POST)

        if form.is_valid():

            return HttpResponse('Successfully signed up')
        return render(request, self.template_name, {'form': form})


@login_required
def createTrial(request):
    if request.method == 'POST':
        form = CreateTrialForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Trial Created successfully')

    else:
        form = CreateTrialForm(initial={'creator': request.user})

    return render(request,'trialapp/createTrial.html',{'form':form})



@login_required
def listTrial(request):
    trials = Trial.objects.filter(creator=request.user)
    operators = Operator.objects.filter(creator=request.user)
    # print(trials)
    for o in operators:
        trials = trials | Trial.objects.filter(creator=o)

    return render(request,'trialapp/listTrial.html',{'trials':trials})


@login_required
def listOperator(request):
    # # print(request.user.has_perm('trialapp.view_operator'))
    # if request.method == 'POST':
    #     # print(id)
    #     form = ListOperatorForm()
    #
    #
    # #else:
    #     #form = DeleteOperatorForm(request.POST)

    operators = Operator.objects.filter(creator=request.user)
    
    return render(request,'trialapp/operators.html',{'operators':operators,})



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



#def enroll(request,title):

#    if request.method == 'POST':
#        form = EnrollmentForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponse('Successfully Enrolled')
    
#    form = EnrollmentForm(initial={'trial':title})
#    return render(request,'trialapp/enrollment.html',{'form':form})

def listEnrollment(request):
    enrolled = Enrollment.objects.all()
    return render(request,'trialapp/listEnrollment.html',{'enrolled':enrolled})


def contact(request, title):
    trial = Trial.objects.get(title=title)
    creator_username = trial.creator
    try:
            creator = Investigator.objects.get(username=creator_username)
            form = ContactForm(initial={'consultant':creator.username,'email':creator.email,})
            return render(request,'trialapp/contact.html',{'form':form})
    except: 
            creator = Operator.objects.get(username=creator_username)
            form = ContactForm(initial={'consultant':creator.username,'email':creator.email,})

            return render(request,'trialapp/contact.html',{'form':form})





# views for testing purpose     GENERIC EDITING VIEW

from django.views.generic.edit import CreateView,UpdateView, FormView
from .models import Patient
from .forms import LoginForm


from django.contrib.auth import authenticate, login, logout

from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



''' generic display views'''



class ListTrials(ListView):
    template_name = 'trialapp/trials.html'
    success_url = '/trialapp'

    def get_queryset(self):
        trials = Trial.objects.filter(creator=self.request.user)
        operators = Operator.objects.filter(creator=self.request.user)
        # print(trials)
        for o in operators:
            trials = trials | Trial.objects.filter(creator=o)

        # return render(request, 'trialapp/listTrial.html', {'trials': trials})
        return trials

class DetailTrial(DetailView):
    template_url = 'trialapp/trial_detail.html'
    model = 'Trial'
    queryset = Trial.objects.all()
    def get_object(self):
        print(self.args)
        print(self.kwargs)
        print(self.request)
        title_ = Trial.objects.get(title=self.kwargs['title'])
        return title_



'''generic editing view'''

class SignupPatient(CreateView):
    form_class = PatientSignupForm
    template_name = 'trialapp/userSignup.html'
    success_url = '/trialapp'


class UpdateOperator(UpdateView):
    model = Operator
    # form_class = OperatorSignupForm
    # template_name = 'trialapp/operator_form.html'
    fields = ['username','first_name','last_name','first_name','email','creator']
    # success_url = '/trialapp'
    #
    # def get(self,*args,**kwargs):
    #     op = self.get_object()
    #     form = OperatorSignupForm(initial={'username':op.username})
    #     return render(self.request, self.template_name,{'form':form})
    #
    #
    #
    #

    def get_initial(self):
        initial = super(UpdateOperator, self).get_initial()
        print('initial data', initial)

        # retrieve current object
        object = self.get_object()

        initial['username'] = object.username
        initial['creator'] = object.creator

        return initial

    def get_object(self, queryset=None):
        obj = Operator.objects.get(id=self.kwargs['pk'])
        print(obj)
        return obj



class Login(FormView):
    form_class = LoginForm
    template_name = 'trialapp/userSignin.html'
    success_url = '/trialapp'

    def form_valid(self,form):
        print('form_valid method')
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            print('logged in')
            login(self.request, user)
        else:
            return HttpResponseRedirect('')

        return super().form_valid(form)

'''generic base view'''
# class Login(View):
#     # form_class = LoginForm
#     success_url = '/trialapp'
#     template_name = 'trialapp/userSignin.html'   #login.html
#     def post(self, request):
#         logout(request)
#         print('post method')
#         form = LoginForm(request.POST)
#         # username = password = ''
#         # form = self.form_class(request.POST)
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#
#         user = authenticate(username=username, password=password)
#         if user is not None and user.is_active:
#             login(request, user)
#             return HttpResponseRedirect(self.success_url)
#         return render(request, self.template_name,{'form':form})
#
#     def get(self, request):
#         form = LoginForm()
#         print(' get method')
#         return render(request, self.template_name,{'form':form})





# class Author(RedirectView):
#     url_pattern = 'dashboard'
#
#     def get_redirect_url(self,*args,**kwargs):
#         return super().get_redirect_url(*args,**kwargs)
from .models import City


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'trialapp/cities.html', {'cities': cities})