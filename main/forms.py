from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Profile Form."""

    class Meta:
        model = Profile
        fields = [
            'name',
            'update',
            'user',
            'image',
        ]
        widgets = {
            'user': forms.HiddenInput(),
        }
