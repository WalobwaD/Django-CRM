# Generated by Django 4.1.2 on 2022-10-17 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='organizer',
            field=models.BooleanField(default=True),
        ),
    ]
