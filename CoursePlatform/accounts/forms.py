from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class FullUserCreationForm(UserCreationForm):
    """
    Extends standard usercreationform by including email address
    """
    CHOICES = (('1', "Register as a Student",), ('2', "Register as a Partner",))
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = User
        fields = ["user_type", "username", "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-Mail'}),
        }


class UserUpdateForm(forms.ModelForm):
    """
    A form for updating common fields for all types of users: email, username
    """

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    """
    A form for updating student's profile details
    """
    profile_pic = forms.ImageField(label='Profile picture', required=False,
                                   error_messages={'invalid': "Image files only"}, widget=forms.FileInput)
    birth_date = forms.DateField()

    class Meta:
        model = Profile
        fields = ['profile_pic', 'first_name', 'last_name', 'gender', 'birth_date', 'country']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'})
        }
