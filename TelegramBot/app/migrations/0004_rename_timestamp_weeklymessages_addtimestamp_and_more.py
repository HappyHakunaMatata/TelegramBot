# Generated by Django 4.2.5 on 2023-09-19 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_weeklymessages_weekname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklymessages',
            old_name='timestamp',
            new_name='AddTimestamp',
        ),
        migrations.RenameField(
            model_name='weeklymessages',
            old_name='message',
            new_name='AddWeek',
        ),
        migrations.RenameField(
            model_name='weeklymessages',
            old_name='weekname',
            new_name='AddWeeklyMessage',
        ),
    ]