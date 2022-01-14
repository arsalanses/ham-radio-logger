# Generated by Django 4.0.1 on 2022-01-14 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_alter_log_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='date',
        ),
        migrations.RemoveField(
            model_name='log',
            name='time',
        ),
        migrations.AddField(
            model_name='log',
            name='datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]