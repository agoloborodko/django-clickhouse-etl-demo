from django_registration.forms import RegistrationForm

from .models import PrototypeUser


class PrototypeUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = PrototypeUser

