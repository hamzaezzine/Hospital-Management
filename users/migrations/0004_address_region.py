# Generated by Django 4.2.9 on 2024-01-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_address_options_alter_doctors_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='region',
            field=models.CharField(default='region', max_length=50),
        ),
    ]
