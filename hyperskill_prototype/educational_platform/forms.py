from django_registration.forms import RegistrationForm
from django.utils import timezone

from .models import PrototypeUser


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
