# Generated by Django 2.1.1 on 2018-09-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbdata', '0002_auto_20180905_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='c_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Changed'),
        ),
    ]
