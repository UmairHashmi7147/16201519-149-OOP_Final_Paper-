# Generated by Django 3.0.2 on 2020-01-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_intoresume_d_resume_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='intoresume',
            name='d_resume_counter',
            field=models.IntegerField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
