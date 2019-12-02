from django import forms
from xplrmain.models import UserPost


class UserPostForm(forms.ModelForm):
    """Render and process a form based on the Page model."""

    class Meta:
        """Meta class to specify form."""

        model = UserPost
        fields = ('coordinates', 'difficulty', 'description', 'time_to_go', 'verified')
