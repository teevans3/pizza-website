from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm



class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='')
    last_name = forms.CharField(max_length=100, required=True, label='')
    email = forms.EmailField(required=True, label='')
    address = forms.CharField(max_length=200, required=True, label='')
    class Meta:
        model = User
        fields = ('first_name',
            'last_name',
            'username',
            'email',
            'address',
            'password1',
            'password2')
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        # Style the registration form
        self.fields['first_name'].widget.attrs.update({'class' : 'register-input', 'placeholder' : 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class' : 'register-input', 'placeholder' : 'Last Name'})
        self.fields['username'].widget.attrs.update({'class' : 'register-input', 'placeholder' : 'Username'})
        self.fields['email'].widget.attrs.update({'class' : 'register-input', 'placeholder' : 'Email'})
        self.fields['address'].widget.attrs.update({'class' : 'register-input', 'placeholder' : 'Address'})
        self.fields['password1'].widget.attrs.update({'class' : 'register-input', 'placeholder' : 'Password'})
        self.fields['password2'].widget.attrs.update({'class' : 'register-input', 'placeholder' : 'Confirm Password'})
        # Remove remaining default labels
        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        # Remove 'helptext' default from form
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        if commit:
            user.save()
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        return user


class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        # Style the password-change form
        self.fields['old_password'].widget.attrs.update({'class': 'pass-change-input-old', 'placeholder': 'Current Password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'pass-change-input-new1', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'pass-change-input-new2', 'placeholder': 'Confirm New Password'})
        # Remove remaining default labels
        self.fields['old_password'].label = ''
        self.fields['new_password1'].label = ''
        self.fields['new_password2'].label = ''
        # Remove 'helptext' default from form
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None
