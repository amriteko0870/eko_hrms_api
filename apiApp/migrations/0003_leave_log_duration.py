# Generated by Django 4.0.3 on 2022-09-16 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0002_user_details_token_user_details_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_log',
            name='DURATION',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
