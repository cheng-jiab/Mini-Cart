# Generated by Django 3.1 on 2021-09-01 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='phone_number',
            new_name='phoneNumber',
        ),
    ]
