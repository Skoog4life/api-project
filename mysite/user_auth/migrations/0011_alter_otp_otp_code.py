# Generated by Django 5.0.6 on 2024-06-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0010_remove_customuser_user_auth_customuser_email_or_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='otp_code',
            field=models.CharField(max_length=20),
        ),
    ]
