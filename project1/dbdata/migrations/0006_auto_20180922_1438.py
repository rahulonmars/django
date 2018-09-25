# Generated by Django 2.1.1 on 2018-09-22 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbdata', '0005_auto_20180906_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='c_date',
            field=models.DateTimeField(verbose_name='Date Changed'),
        ),
        migrations.AlterField(
            model_name='table1',
            name='fname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Verbose_Name'),
        ),
    ]