from django_registration.forms import RegistrationForm
from django import forms
from django.utils import timezone

from .models import PrototypeUser, PrototypeEvent


class PrototypeUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = PrototypeUser

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.registration_date = timezone.now()
        user.is_guest = 0
        if commit:
            user.save()
        return user


class TaskSubmitForm(forms.Form):
    CHOICES = [(1, 'Submit'),
               (2, 'Resolve')]
    action = forms.CharField(widget=forms.RadioSelect(choices=CHOICES))
