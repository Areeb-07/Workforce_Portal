# Generated by Django 4.0.4 on 2022-10-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('departments', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('roll_number', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('departments', models.CharField(blank=True, max_length=255)),
                ('current_task', models.CharField(blank=True, max_length=255)),
                ('cg', models.CharField(blank=True, max_length=255)),
                ('progress', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
