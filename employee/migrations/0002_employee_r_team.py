# Generated by Django 2.2.6 on 2019-10-29 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='r_team',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='teams.Teams'),
            preserve_default=False,
        ),
    ]