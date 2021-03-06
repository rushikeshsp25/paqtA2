# Generated by Django 2.2.1 on 2019-05-06 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
