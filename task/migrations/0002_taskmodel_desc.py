# Generated by Django 4.0.6 on 2022-07-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='desc',
            field=models.CharField(default='', max_length=250),
        ),
    ]
