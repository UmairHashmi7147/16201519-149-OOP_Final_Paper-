# Generated by Django 3.0.3 on 2020-02-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0059_intoresume_d_resume_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intoresume',
            name='d_resume_profile',
            field=models.ImageField(blank=True, null=True, upload_to='static/profile_image'),
        ),
    ]
