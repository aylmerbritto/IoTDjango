from .models import realTimeModel
from django import forms

class realTimeForm(forms.ModelForm):
    class Meta():
        model = realTimeModel
        fields=['temperature','humidity','pressure']
        print(fields)
