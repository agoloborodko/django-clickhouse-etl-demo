from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class PrototypeTask(models.Model):
    """
    У класса "Задача" будет только идентификатор (id),
    никаких других полей не требуется
    """
    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this task."""
        return reverse('educational_platform:task-detail', args=[str(self.id)])


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
    target_id = models.ForeignKey(PrototypeTask, on_delete=models.PROTECT)
    user_id = models.ForeignKey(PrototypeUser, on_delete=models.PROTECT)
