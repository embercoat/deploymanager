# Generated by Django 2.0.1 on 2018-01-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20180120_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationserver',
            name='lastScanned',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='lastScanned',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
