
from django import forms

from .models import UserProfile, cheackout


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'



class cheackout(forms.ModelForm):
    class Meta:
        model = cheackout
        fields = '__all__'
        
# forms.py

from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

          