# forms.py
from django import forms
from .models import Customer
from .models import CustomerProfile, KidProfile


class KidProfileForm(forms.ModelForm):
    class Meta:
        model = KidProfile
        fields = ['profilename', 'avatar']


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'email', 'username', 'password', 'DoB', 'phonenumber']
        widgets = {
            'password': forms.PasswordInput(),
            'DoB': forms.DateInput(attrs={'type': 'date'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class CustomerProfileForm(forms.ModelForm):
    confirm_pin = forms.CharField(widget=forms.PasswordInput, label='Confirm PIN')
    pin = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomerProfile
        fields = ['profilename', 'pin', 'confirm_pin', 'avatar']

    def clean(self):
        cleaned_data = super().clean()
        pin = cleaned_data.get('pin')
        confirm_pin = cleaned_data.get('confirm_pin')

        if pin and confirm_pin and pin != confirm_pin:
            raise forms.ValidationError("PIN and Confirm PIN do not match.")

class PINVerificationForm(forms.Form):
    pin = forms.CharField(widget=forms.PasswordInput)