# Generated by Django 3.1.5 on 2021-05-19 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
    ]