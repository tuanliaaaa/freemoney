# Generated by Django 4.2.5 on 2023-10-10 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmoney',
            name='nameAdd',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='submoney',
            name='nameSub',
            field=models.CharField(max_length=225),
        ),
    ]
