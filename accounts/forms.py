from django import forms

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """Form for UserProfile."""

    class Meta:
        """Metadata about this form."""

        model = UserProfile
        fields = ('photography_type', 'risk_level')
