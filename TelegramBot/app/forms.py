"""
Definition of forms.
"""

from sqlite3 import Timestamp
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import DailyMessages, DateTimeMessages, WeeklyMessages
from django.core.validators import MinValueValidator, MaxValueValidator


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class AddDailyMessagesForm(forms.ModelForm):
    text = forms.CharField(max_length=1000)
    timestamp =  forms.DateTimeField(input_formats=['%H:%M'])
    class Meta:
        model = DailyMessages 
        fields = ['text', 'timestamp']

class EditDailyMessagesForm(forms.Form):
    key = forms.IntegerField()
    edittext = forms.CharField(max_length=1000)
    edittimestamp =  forms.DateTimeField(input_formats=['%H:%M'])


class DeleteDailyMessagesForm(forms.Form):
    primaryKey = forms.IntegerField()


class AddDatetimeMessagesForm(forms.ModelForm):
    textfield = forms.CharField(max_length=1000)
    timestampfield =  forms.DateTimeField(input_formats=['%H:%M'])
    datefield =  forms.DateField(input_formats=['%Y-%m-%d'])
    class Meta:
        model = DateTimeMessages 
        fields = ['textfield', 'timestampfield', 'datefield']

class EditDatetimeMessagesForm(forms.Form):
    idDatetime = forms.IntegerField()
    textfield = forms.CharField(max_length=1000)
    timestampfield =  forms.DateTimeField(input_formats=['%H:%M'])
    editdatefield =  forms.DateField(input_formats=['%Y-%m-%d'])
    

class DeleteDatetimeMessagesForm(forms.Form):
    Pkey = forms.IntegerField()

        
class SendMessageForm(forms.Form):
    sendMessage = forms.CharField()

class AuthTelethonForm(forms.Form):
    code = forms.IntegerField(
        widget=forms.NumberInput(attrs={'pattern': '^[0-9]{6,6}$', 'title': 'Number must contains only six degits'})
    )


class AddWeeklyMessagesForm(forms.ModelForm):
    AddWeeklyMessage = forms.CharField(max_length=1000)
    AddTimestamp =  forms.DateTimeField(input_formats=['%H:%M'])
    AddWeek =  forms.CharField(max_length=1000)
    class Meta:
        model = WeeklyMessages 
        fields = ['AddWeeklyMessage', 'AddTimestamp', 'AddWeek']
        

class DeleteWeeklyForm(forms.Form):
    idDeleteWeekly = forms.IntegerField()
    
class EditWeeklyMessagesForm(forms.Form):
    idWeekly = forms.IntegerField()
    AddWeeklyMessage = forms.CharField(max_length=1000)
    AddTimestamp =  forms.DateTimeField(input_formats=['%H:%M'])
    AddWeek = forms.CharField(max_length=1000)
    