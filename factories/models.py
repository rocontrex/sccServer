from django.db import models
from django.contrib.auth.models import User

class Factories(models.Model):
    s_name = models.CharField(
        max_length=100,
        null = False
    )

    r_user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    objects = models.Manager()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'factories'
