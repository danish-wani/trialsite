from django.forms import ModelForm
from django import forms
from .models import Investigator, Operator, Trial, Enrollment
from .models import Country, City

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

# import django-select2

class CreateTrialForm(ModelForm):
    class Meta:
        model = Trial
        fields = ('title','description','country','city','creator',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()


        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
    # country = forms.ModelChoiceField(
    #     queryset=Country.objects.all(),
    #     label="Country",
    #     widget=ModelSelect2Widget(
    #         search_fields=['name__icontains'],
    #         dependent_fields={'city': 'cities'},
    #     )
    # )
    #
    # city = forms.ModelChoiceField(
    #     queryset=City.objects.all(),
    #     label="City",
    #     widget=ModelSelect2Widget(
    #         search_fields=['name__icontains'],
    #         dependent_fields={'country': 'country'},
    #         max_results=500,
    #     )
    # )


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