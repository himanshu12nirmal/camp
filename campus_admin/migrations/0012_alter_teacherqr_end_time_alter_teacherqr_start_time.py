# Generated by Django 4.1.7 on 2023-05-24 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0011_alter_teacherqr_end_time_alter_teacherqr_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherqr',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='teacherqr',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
