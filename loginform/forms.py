from .models import User
from django import forms

class form(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
