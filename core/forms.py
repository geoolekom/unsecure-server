from django import forms


class BashForm(forms.Form):
    input = forms.CharField(max_length=200)
