# Generated by Django 3.1.5 on 2021-05-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
