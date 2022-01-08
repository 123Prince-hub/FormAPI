from django import forms
from django.forms import fields
from django.forms.formsets import ORDERING_FIELD_NAME
from django.forms.widgets import CheckboxInput, EmailInput, FileInput, HiddenInput, Textarea, URLInput

class StudentRegistration(forms.Form):
    name = forms.CharField()
    # name = forms.CharField(widget=forms.PasswordInput()/HiddenInput()/Textarea()/CheckboxInput()/FileInput()/EmailInput()/URLInput())  # field input using widgits in field
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'cls', 'id':'my_ID'}))
    # name = forms.CharField(label='Your Name')   # Declare Label of field
    # name = forms.CharField(label_suffix='')   # replace Label of field to colon to any charector
    # name = forms.CharField(required=False)   # required attribut false by default true
    # name = forms.CharField(disabled=True)   # visiblity attribut true by default false
    # email = forms.EmailField()
    # mobile = forms.IntegerField()
    # key = forms.CharField(widget=forms.HiddenInput()) 
    # email = forms.EmailField(initial='princekirad11@gmail.com')      # default value in form field
    # email = forms.EmailField(help_text='is field me 30 letter hi lik skte h')      # help text in form field
    # user_password = forms.CharField()   # underscore changed into space