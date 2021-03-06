# Generated by Django 2.1 on 2018-10-09 06:40

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Investigator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('can_create_trial', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trialapp.Investigator')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trialapp.City')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trialapp.Country')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='trials_enrolled',
            field=models.ManyToManyField(to='trialapp.Trial'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='trial',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trialapp.Trial'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trialapp.Message'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='receiver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversation',
            name='sender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trialapp.Country'),
        ),
    ]
