# Generated by Django 5.0.4 on 2024-04-26 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='principal_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puser', models.CharField(max_length=100)),
                ('ppass', models.CharField(max_length=100)),
            ],
        ),
    ]
