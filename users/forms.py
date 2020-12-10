from .models import Profile
from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


class UserLoginForm(AuthenticationForm):
    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        fields = ['username', 'password', 'captcha']


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        # for fieldname in ['username', 'password1', 'password2']:
        self.fields['password1'].help_text = 'Please keep your password dissimilar from your other info, 8 Characterers Minium, Not entirely Numeric, also please don\'t use common passwords for security purposes'
    email = forms.EmailField()

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "Entered Email already exists ! Please Login")
        return self.cleaned_data

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


class ProfileForm(forms.ModelForm):

    dob = forms.DateField(
        localize=True,
        label='Date of Birth',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
    )

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = Profile
        fields = ['gender', 'phone_no', 'aadhar_card', 'dob', 'address', 'city', 'bloodType',
                  'allergy', 'alzheimer', 'asthma', 'diabetes', 'stroke', 'captcha']
        labels = {
            'gender': 'Gender',
            'phone_no': 'Phone No.',
            'address': 'Address',
            'stroke': 'Heart Stroke',
            'city': 'City Living IN',
            'bloodType': 'Blood Type',
        }
