# Generated by Django 5.0.1 on 2024-01-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_reste_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reste_token',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
