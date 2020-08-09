from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import PrototypeUser


@receiver(pre_save, sender=PrototypeUser)
def add_user_registration_date(sender, **kwargs):
    print('PrototypeUser instance saved')
