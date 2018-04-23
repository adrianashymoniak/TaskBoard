# Generated by Django 2.0.1 on 2018-04-23 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('New', 'new'), ('In progress', 'in progress'), ('Done', 'done')], max_length=11),
        ),
    ]