# Generated by Django 4.0.5 on 2022-06-22 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=32)),
                ('course', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('weather', models.CharField(max_length=32)),
                ('teesPlayed', models.CharField(max_length=32)),
            ],
        ),
    ]
