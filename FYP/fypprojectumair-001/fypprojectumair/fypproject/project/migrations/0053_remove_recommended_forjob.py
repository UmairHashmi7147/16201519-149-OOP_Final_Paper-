# Generated by Django 3.0.3 on 2020-02-27 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0052_recommended_forjob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommended',
            name='forjob',
        ),
    ]
