# Generated by Django 3.0.2 on 2020-01-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_intoresume_d_resume_career_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_career_level_periority',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_degree_level_periority',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_experience_periority',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_prefrence_periority',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_skills_periority',
            field=models.IntegerField(max_length=50),
        ),
    ]
