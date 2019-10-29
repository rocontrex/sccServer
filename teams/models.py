from django.db import models
from django.contrib.auth.models import User

class Teams(models.Model):
    s_name = models.CharField(max_length=100)
    i_indicador = models.IntegerField
    r_user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'teams'
