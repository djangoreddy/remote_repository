# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-01-06 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ENQdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('course', multiselectfield.db.fields.MultiSelectField(choices=[('PYTHON', 'Python'), ('DJANGO', 'Django'), ('UI', 'Ui'), ('REST API', 'Rest api')], max_length=200)),
                ('teacher', multiselectfield.db.fields.MultiSelectField(choices=[('NAGUR', 'Nagur'), ('DURGA', 'Durga'), ('SAI', 'Sai'), ('HARI', 'Hari')], max_length=200)),
                ('braches', multiselectfield.db.fields.MultiSelectField(choices=[('HYD', 'Hyd'), ('Bang', 'Bang'), ('VSKP', 'Vskp')], max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('start_date', models.DateField(max_length=100)),
            ],
        ),
    ]
