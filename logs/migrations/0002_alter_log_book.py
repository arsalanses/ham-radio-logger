# Generated by Django 3.2.3 on 2022-01-13 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='logs.logbook'),
        ),
    ]
