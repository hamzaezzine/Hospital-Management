# Generated by Django 4.2.9 on 2024-01-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
    ]
