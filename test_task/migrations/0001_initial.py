# Generated by Django 4.1 on 2022-08-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100, verbose_name='Логин')),
                ('user_id', models.IntegerField(unique=True)),
            ],
        ),
    ]
