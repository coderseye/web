# Generated by Django 4.0.6 on 2022-08-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('number', models.CharField(max_length=12)),
                ('mess', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
