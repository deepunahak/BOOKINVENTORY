from django import forms


class UserRegisterForm(forms.Form):
    name = forms.CharField(max_length=127)
    email = forms.EmailField(max_length=127)
    password = forms.CharField(max_length=127)


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=127)
    password = forms.CharField(max_length=127)
