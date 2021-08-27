# Generated by Django 3.1.5 on 2021-05-27 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210525_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.CharField(default='', max_length=100)),
                ('loantype', models.CharField(default='', max_length=100)),
                ('amount', models.CharField(default='', max_length=100)),
                ('id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
    ]