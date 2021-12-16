from django import forms
from django.forms import ModelForm

from .models import *

class questionForm(forms.ModelForm):

    class Meta:
        model = question
        fields = '__all__'