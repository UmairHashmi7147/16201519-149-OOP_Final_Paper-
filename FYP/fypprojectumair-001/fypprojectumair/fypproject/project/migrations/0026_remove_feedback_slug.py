# Generated by Django 3.0.2 on 2020-02-11 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0025_feedback_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='slug',
        ),
    ]
