# Generated by Django 2.2 on 2020-08-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0072_auto_20200818_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Pcnic',
            field=models.CharField(max_length=15),
        ),
    ]
