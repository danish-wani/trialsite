from django.forms import ModelForm
from django import forms
from .models import Investigator, Operator, Trial, Enrollment

class InvestigatorForm(ModelForm):
    class Meta:
        model = Investigator
        fields = ['username','password','email']


from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Investigator, Patient 

class InvestigatorSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Investigator
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email',)


class OperatorSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Operator
        fields = UserCreationForm.Meta.fields +('creator','first_name','last_name','email',)


class ListOperatorForm():
    class Meta():
        model = Operator
        fields = ('id','username',)

class ListTrialForm():
    class Meta():
        model = Trial
        fields = ('title','description','country','city','creator',)


# class EditOperatorForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = UserChangeForm.Meta.fields
        

class CreateTrialForm(ModelForm):
    class Meta:
        model = Trial
        fields = ('title','description','country','city','creator',)


class PatientSignupForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Patient
        fields = UserCreationForm.Meta.fields +('trials_enrolled','first_name','last_name','email',)
        
class EnrollmentForm(ModelForm):
    class Meta:
        model = Enrollment
        fields = ('trial','patient_name','email',)

class ContactForm(forms.Form):
    consultant = forms.CharField(label='Consultant',max_length=15)
    email = forms.EmailField(label='Email')

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    # class Meta:
    #     widgets = {
    #         'password': forms.PasswordInput(),
    #     }