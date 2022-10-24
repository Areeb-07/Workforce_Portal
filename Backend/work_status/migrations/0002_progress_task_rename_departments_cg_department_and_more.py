# Generated by Django 4.0.4 on 2022-10-23 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_number', models.CharField(max_length=30)),
                ('task_id', models.CharField(max_length=30)),
                ('progress', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=30)),
                ('task', models.CharField(max_length=255)),
                ('sub_task', models.CharField(max_length=255)),
                ('cg_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameField(
            model_name='cg',
            old_name='departments',
            new_name='department',
        ),
        migrations.RemoveField(
            model_name='coordinator',
            name='cg',
        ),
        migrations.RemoveField(
            model_name='coordinator',
            name='current_task',
        ),
        migrations.RemoveField(
            model_name='coordinator',
            name='progress',
        ),
        migrations.AddField(
            model_name='cg',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]