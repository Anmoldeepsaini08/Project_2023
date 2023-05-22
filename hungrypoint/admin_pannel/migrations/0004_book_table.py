# Generated by Django 4.2 on 2023-05-22 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_pannel', '0003_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=20)),
                ('user_phone', models.IntegerField()),
                ('date', models.CharField(max_length=230)),
                ('time', models.CharField(default='', max_length=12)),
                ('people', models.IntegerField(default='')),
            ],
        ),
    ]
