from django import forms


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=32, label="Username", required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, label="Password", required=True)
    first = forms.CharField(max_length=32, label="First Name", required=True)
    last = forms.CharField(max_length=32, label="Last Name", required=True)
    email = forms.EmailField(label="Email", required=True)