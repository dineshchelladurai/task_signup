# Generated by Django 5.0 on 2024-03-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=16)),
                ('confirm_password', models.CharField(max_length=16)),
            ],
        ),
    ]
