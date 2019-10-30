from django.db import models
from django.contrib.auth.models import User
from factories.models import Factories

class Teams(models.Model):
    s_name = models.CharField(
        null = False,
        max_length=100
    )

    i_indicador = models.IntegerField

    r_user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    r_factory = models.ForeignKey(
        Factories,
        on_delete=models.DO_NOTHING
    )

    objects = models.Manager()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'teams'
