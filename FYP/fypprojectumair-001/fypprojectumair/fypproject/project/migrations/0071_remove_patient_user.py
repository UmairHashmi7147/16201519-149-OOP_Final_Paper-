# Generated by Django 2.2 on 2020-08-18 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0070_department_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
    ]