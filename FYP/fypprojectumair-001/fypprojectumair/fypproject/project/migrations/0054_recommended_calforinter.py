# Generated by Django 3.0.3 on 2020-02-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0053_remove_recommended_forjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommended',
            name='calforinter',
            field=models.BooleanField(default=False),
        ),
    ]
