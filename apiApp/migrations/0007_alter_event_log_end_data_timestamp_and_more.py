# Generated by Django 4.0.3 on 2022-09-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0006_timesheet_log_date_alter_timesheet_log_clock_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_log',
            name='END_DATA_TIMESTAMP',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='event_log',
            name='START_DATE_TIMESTAMP',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='leave_log',
            name='END_DATE_TIMESTAMP',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='leave_log',
            name='START_DATE_TIMESTAMP',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='overtime_log',
            name='DATE_TIMESTAMP',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='overtime_log',
            name='DURATION',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='task_log',
            name='DATE_TIMESTAMP',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='timesheet_log',
            name='CLOCK_IN_TIMESTAMP',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='timesheet_log',
            name='CLOCK_OUT_TIMESTAMP',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='timesheet_log',
            name='DATE',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='JOINING_DATE_TIMESTAMP',
            field=models.BigIntegerField(blank=True),
        ),
    ]