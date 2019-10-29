from django.db import models
from django.contrib.auth.models import User
from teams.models import Teams

class Employee(models.Model):
    s_name = models.CharField(max_length=100)
    s_phone = models.CharField(max_length=100)
    s_mail = models.CharField(max_length=100)
    s_registration = models.CharField(max_length=100)
    d_admission_date = models.DateTimeField()
    d_register_date = models.DateTimeField(auto_now_add=True)
    b_in_charge = models.BooleanField(default=False)
    r_user = models.ForeignKey(User, on_delete=models.CASCADE)
    r_team = models.ForeignKey(Teams, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'employee'
