# Generated by Django 2.2 on 2020-08-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0073_auto_20200818_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='Paddress',
        ),
        migrations.RemoveField(
            model_name='department',
            name='Pcnic',
        ),
        migrations.AlterField(
            model_name='department',
            name='No_of_beds',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='department',
            name='No_of_employees',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='No_of_patients',
            field=models.IntegerField(default=0),
        ),
    ]
