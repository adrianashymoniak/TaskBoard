# Generated by Django 2.0.1 on 2018-03-11 17:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20180215_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_published',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
