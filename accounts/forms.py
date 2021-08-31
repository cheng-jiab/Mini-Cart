from django import forms
from .models import Account
#ref: https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
class RegistrationForm(forms.ModelForm):
      
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class': 'form-control'
    }))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat Password',
        'class': 'form-control'
    }))
    class Meta:
        model = Account
        fields = ['firstName', 'lastName', 'phoneNumber', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['lastName'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['phoneNumber'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirmPassword = cleaned_data.get('confirmPassword')
        if password != confirmPassword:
            raise forms.ValidationError(
                'Password does not match'
            )
 
