# Generated by Django 4.2.5 on 2023-11-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_progressbarpk_progressbarstatus_progressbarpkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='KickTimeTable',
            fields=[
                ('PKey', models.AutoField(primary_key=True, serialize=False)),
                ('Time', models.DateTimeField()),
            ],
        ),
    ]
