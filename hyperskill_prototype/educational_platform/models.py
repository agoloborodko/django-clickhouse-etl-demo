from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from lazysignup.signals import converted


class PrototypeTask(models.Model):
    """
    У класса "Задача" будет только идентификатор (id),
    никаких других полей не требуется
    """
    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this task."""
        return reverse('task-detail', args=[str(self.id)])


class PrototypeUser(AbstractUser):
    registration_date = models.DateTimeField(null=True)
    is_guest = models.BooleanField(default=True)


class PrototypeEvent(models.Model):
    ACTIONS = [
        (0, 'Увидеть задачу'),
        (1, 'Отправить попытку решения'),
        (2, 'Решить задачу')
    ]
    time = models.DateTimeField()
    action_id = models.SmallIntegerField(choices=ACTIONS)
    target = models.ForeignKey(PrototypeTask, on_delete=models.PROTECT)
    user = models.ForeignKey(PrototypeUser, on_delete=models.PROTECT)


@receiver(converted)
def add_converted_user_registration_date(sender, **kwargs):
    user = kwargs['user']
    if not user.registration_date:
        user.registration_date = timezone.now()
        user.is_guest = 0
        user.save()
