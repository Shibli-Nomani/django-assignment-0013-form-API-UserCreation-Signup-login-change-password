# Generated by Django 4.2 on 2023-05-16 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField()),
                ('client_name', models.CharField(max_length=50)),
                ('client_email', models.EmailField(max_length=35)),
                ('batch', models.IntegerField()),
                ('destination', models.CharField(max_length=25)),
            ],
        ),
    ]
