# Generated by Django 4.0.3 on 2022-09-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0003_leave_log_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='overtime_log',
            name='DATE',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overtime_log',
            name='DATE_TIMESTAMP',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
