# Generated by Django 4.1.1 on 2022-09-28 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('address', models.TextField(blank=True, max_length=500)),
                ('bio', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'custom_user',
            },
        ),
    ]
