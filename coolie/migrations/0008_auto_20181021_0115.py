# Generated by Django 2.0.1 on 2018-10-21 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolie', '0007_auto_20181020_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='dropTime',
            field=models.DateTimeField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='flagIn',
            field=models.CharField(choices=[('Platform to Outside', 'Outside to Platform')], default='Platform to Outside', max_length=30),
        ),
    ]