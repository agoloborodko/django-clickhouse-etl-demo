from django.db import models


class PrototypeTask(models.Model):
    """
    У класса "Задача" будет только идентификатор (id),
    никаких других полей не требуется
    """
    def __str__(self):
        return str(self.pk)


