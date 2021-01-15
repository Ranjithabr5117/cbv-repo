# Generated by Django 3.1.3 on 2020-12-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('no', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('sal', models.FloatField()),
                ('dept', models.CharField(max_length=50)),
            ],
        ),
    ]
