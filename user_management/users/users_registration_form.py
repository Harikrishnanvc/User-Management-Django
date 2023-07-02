from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, RegexValidator, MaxLengthValidator, MinLengthValidator

from .models import Users


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    mobile = forms.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(10)])

    class Meta:
        model = Users
        fields = ['first_name', 'last_name',
                  'email', 'password', 'user_role',
                  'country', 'nationality', 'mobile']

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile:
            raise forms.ValidationError('Phone umber is required.')
        if Users.objects.filter(mobile=mobile).exists():
            raise ValidationError('This Phone number is already registered.')
        return mobile

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('E-mail is required.')
        if Users.objects.filter(email=email).exists():
            raise ValidationError('This email is already registered.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            try:
                validate_password(password)
            except forms.ValidationError as validation_error:
                raise forms.ValidationError(validation_error.error_list[0], code='invalid')
        return password


class RegistrationFormFields(forms.Form):
    ROLES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
        ('editor', 'Editor'),
    )
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email', validators=[EmailValidator])
    user_role = forms.ChoiceField(label='Role', choices=ROLES)
    country = forms.CharField(label='Country')
    nationality = forms.CharField(label='Nationality')
    mobile = forms.CharField(label='Mobile',
                             validators=[RegexValidator(r'^[0-9]+$',
                                                        'Enter a Valid Phone Number')])
    password = forms.CharField(label='Password', widget=forms.PasswordInput, )
