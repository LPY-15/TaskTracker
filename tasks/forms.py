from django import forms
from . import models

class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = ['first_name', 'last_name', 'email', 'password']