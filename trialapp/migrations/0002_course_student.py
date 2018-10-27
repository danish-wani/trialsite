# Generated by Django 2.1 on 2018-10-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trialapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('semester', models.CharField(max_length=10)),
                ('courses', models.ManyToManyField(to='trialapp.Course')),
            ],
        ),
    ]