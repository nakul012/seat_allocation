# Generated by Django 4.0.2 on 2022-02-28 21:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seathistory',
            name='filled_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='seathistory',
            name='vacant_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
