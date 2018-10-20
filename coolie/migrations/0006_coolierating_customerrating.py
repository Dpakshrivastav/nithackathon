# Generated by Django 2.0.1 on 2018-10-20 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coolie', '0005_employee_contactno'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoolieRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(null=True)),
                ('coolieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coolie.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(null=True)),
                ('coolieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coolie.Employee')),
            ],
        ),
    ]