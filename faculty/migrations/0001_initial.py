# Generated by Django 5.0.4 on 2024-04-26 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculty_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuser', models.CharField(max_length=100)),
                ('fpass', models.CharField(max_length=100)),
            ],
        ),
    ]
