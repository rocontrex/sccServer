from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    s_name = models.CharField(
        max_length = 100,
        null = False,
        blank = False
    )

    s_phone = models.CharField(
        max_length = 30,
        null = False,
        blank = False
    )

    s_mail = models.CharField(
        max_length = 100,
        null = False,
        blank = False
    )

    s_registration = models.CharField(
        null = False,
        blank = False,
        max_length=100
    )

    d_admission_date = models.DateTimeField(
        null = False,
        blank = False
    )

    d_register_date = models.DateTimeField(
        auto_now_add = True
    )

    b_in_charge = models.BooleanField(
        default = False
    )

    b_has_team = models.BooleanField(
        default = False,
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
        db_table = 'employee'
