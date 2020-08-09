from django.db import models


class PrototypeTask(models.Model):
    """
    У класса "Задача" будет только идентификатор (id),
    никаких других полей не требуется
    """
    def __str__(self):
        return str(self.pk)


class PrototypeUser(models.Model):
    """
    Этот класс описывает не настоящих пользователей с логинами, полями
    и security issues, а их массово генерируемые прототипы.
    Использовать встроенную в django пользовательскую модель
    для случайцно сгенерированных пользователей будет дорого.
    """
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    join_date = models.DateTimeField(auto_now_add=True)
    registration_date = models.DateTimeField(null=True)
    is_guest = models.BooleanField(default=True)

    class Meta:
        constraints = [
            # CHECK (is_guest or not (name is null or email is null or registration_date is null))
            models.CheckConstraint(
                check=models.Q(
                    is_guest=True,
                )
                | models.Q(
                    is_guest=False,
                    name__isnull=False,
                    email__isnull=False,
                    registration_date__isnull=False
                ),
                name='only_guest_can_be_nullable'
            ),
        ]
    # TODO: реализовать boolean-like поведение integer-поля is_guest

    def __str__(self):
        if self.is_guest:
            return f'Guest #{self.pk}'
        else:
            return self.name


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
