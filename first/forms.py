from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from first.models import post
class signup_form(forms.ModelForm):
    re_enter_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password'}),
        label="Confirm Password",
        error_messages={'required': 'Please confirm your password.'},
    )
    username = forms.CharField(
        max_length=150,  # Adjust the max length as needed
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        error_messages={
            'required': 'Please enter a username.',
        },
    )

    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password']
        widgets={
            'password':forms.PasswordInput(attrs={'placeholder':'enter password'})
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('This username is already taken. Please choose another one.')
        return username

class Post_form(forms.ModelForm):
    class Meta:
        model=post
        fields=['image','title','body','publish','status']