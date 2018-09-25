from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

from django.contrib.auth.models import Permission, User

class Trial(models.Model):
    title = models.CharField(max_length=100,primary_key=True)
    description = models.TextField()
    country = models.CharField(max_length=80)
    city = models.CharField(max_length=90)
    creator = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    
    def __str__(self):
        return self.title


class TrialList(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title




class Investigator(User):
    is_superuser = True

    def __str__(self):
        return self.username

class Operator(User):
    creator = models.ForeignKey('Investigator',on_delete=models.CASCADE)
    is_operator = True
    can_create_trial = models.BooleanField(default= False)
   
    def __str__(self):
        return self.username

class Patient(User):
    trials_enrolled = models.ManyToManyField('Trial',)
   

    def __str__(self):
        return 'Patient'

class Message(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class Conversation(models.Model):
    sender = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Sender')
    receiver = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Receiver')
    message = models.ForeignKey('Message',on_delete=models.CASCADE)

    def __str__(self):
        return self.sender+" to "+self.receiver+":" + self.message
