# forms create file
from django import forms

class sum_form(forms.Form):
    num1 = forms.CharField(label='Value1', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    num2 = forms.CharField(label='Value2', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))