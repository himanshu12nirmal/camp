# Generated by Django 4.1.7 on 2023-05-23 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0007_alter_timetable_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='room',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]