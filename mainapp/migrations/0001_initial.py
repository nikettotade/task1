# Generated by Django 4.1.6 on 2023-02-04 07:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(default=datetime.datetime(2023, 2, 4, 7, 33, 27, 261860, tzinfo=datetime.timezone.utc))),
                ('update_at', models.DateTimeField(default=datetime.datetime(2023, 2, 4, 7, 33, 27, 261860, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('enrollment', models.CharField(max_length=100, unique=True)),
                ('create_at', models.DateTimeField(default=datetime.datetime(2023, 2, 4, 7, 33, 27, 261860, tzinfo=datetime.timezone.utc))),
                ('update_at', models.DateTimeField(default=datetime.datetime(2023, 2, 4, 7, 33, 27, 261860, tzinfo=datetime.timezone.utc))),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.school')),
            ],
        ),
    ]
