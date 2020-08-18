# Generated by Django 2.2 on 2020-08-18 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0069_job_request_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pid', models.IntegerField(max_length=15)),
                ('Pname', models.CharField(blank=True, max_length=15)),
                ('PFathername', models.CharField(blank=True, max_length=15)),
                ('Pphone', models.IntegerField(max_length=15)),
                ('Page', models.IntegerField()),
                ('Pgender', models.IntegerField(max_length=15)),
                ('Pcnic', models.IntegerField(max_length=15)),
                ('Paddress', models.CharField(blank=True, max_length=45)),
                ('Pdisease', models.CharField(blank=True, max_length=35)),
                ('active', models.BooleanField(default=True)),
                ('modified_when', models.DateField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dname', models.CharField(blank=True, max_length=15)),
                ('Dtype', models.CharField(blank=True, choices=[('M', 'Medical'), ('S', 'Surgicsal'), ('O', 'OTP'), ('I', 'ICU'), ('IT', 'ITC')], max_length=6)),
                ('No_of_employees', models.IntegerField(max_length=15)),
                ('No_of_beds', models.IntegerField()),
                ('No_of_patients', models.IntegerField(max_length=15)),
                ('Pcnic', models.IntegerField(max_length=15)),
                ('Paddress', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('Pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Patient')),
            ],
        ),
    ]
