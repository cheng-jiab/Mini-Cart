# Generated by Django 3.1 on 2021-09-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variationCategory',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size')], default='size', max_length=100),
            preserve_default=False,
        ),
    ]