from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="name", max_length=256)
    check = forms.BooleanField()