from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(label='Password', max_length=100)

class UserLoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class HintForm(forms.Form):
    answer = forms.CharField(label='Answer', max_length=100)

class RoundForm(forms.Form):
    answer = forms.CharField(label='Answer', max_length=100)