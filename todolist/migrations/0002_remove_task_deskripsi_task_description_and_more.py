# Generated by Django 4.1 on 2022-10-13 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='deskripsi',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
